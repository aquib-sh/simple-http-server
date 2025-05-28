import socket
import os
import sys
import json

from http_status import HttpStatus
from request_parser import RequestParser, HttpMethodType
from response_builder import HttpResponseBuilder


class HttpServer:
    def __init__(self):
        self.SERVER_HOST = '0.0.0.0'
        self.SERVER_PORT = 8001
        self.STATIC_DATA_FOLDER = 'static'

        self.SUPPORTED_CONTENT_TYPES = self.__load_config('content_types.json')
        self.sock = None


    def __load_config(self, filename: str):
        return json.load(open(filename))


    def build_server(self):
        """Build a socket of IPV4 and TCP."""
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((self.SERVER_HOST, self.SERVER_PORT))
        sock.listen(1)
        print("Server is listening on %s..." % self.SERVER_PORT)
        return sock
    

    def resource_exists(self, resource: str) -> bool:
        return os.path.exists(resource)
    
    
    def build_resource_path(self, resource: str) -> str:
        return os.path.join(self.STATIC_DATA_FOLDER, resource[1:])
    
    
    def fetch_resource(self, full_resource_path: str) -> bytes | None:
        """Fetches the content from the content from the resource and sends it as bytes."""
    
        fp = None
    
        fp = open(file=full_resource_path, mode='rb')
    
        content = fp.read()
        fp.close()
    
        return content
    
    
    def get_resource_content_type(self, resource) -> str | None:
        """Gets the content type of resource."""
    
        file_format = ""
    
        i = len(resource)-1
    
        while ((c := resource[i]) != "."):
            file_format = c + file_format 
            i -= 1
    
        print(file_format)
    
        if file_format not in self.SUPPORTED_CONTENT_TYPES:
            return None
    
        return self.SUPPORTED_CONTENT_TYPES[file_format]
    
        
    def run(self):
        """Accepts connections in a continous running"""

        self.sock = self.build_server()
        responseBuilder = HttpResponseBuilder()

        sock = self.sock
    
        while True:
            client_connection, client_address = sock.accept()
            print(client_address)
    
            request = client_connection.recv(1024).decode()

            if len(request) == 0:
                continue

            parsed_request = RequestParser.parse(request)
            print(parsed_request)
   
            content = None
            content_type = None
    
            # Handle get request
            if parsed_request.method is HttpMethodType.GET:
                full_resource_path = self.build_resource_path(parsed_request.path)
    
                if self.resource_exists(full_resource_path):
                    content_type = self.get_resource_content_type(full_resource_path)
                    content = self.fetch_resource(full_resource_path)
    
            headers = {}
            response = None

            if not content:
                headers["Content-Type"] = "application/text"
                response = responseBuilder.build(HttpStatus.NOT_FOUND, "Resource Not Found")

            elif content_type:
                headers["Content-Type"] = content_type
                response = responseBuilder.build(HttpStatus.OK, content, headers)
    
            client_connection.sendall(response)
    
            # Free up the connection
            client_connection.close()

    def shutdown(self):
        self.sock.close()



if __name__ == "__main__":
        server = HttpServer()

        try:
            server.run()
        except Exception as e:
            print(e.with_traceback)
            server.shutdown()
