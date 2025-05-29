import json
import socket
import startup

from controllers.user_controller import UserController
from http_status import HttpStatus
from request_parser import RequestParser, HttpMethodType
from response_builder import HttpResponseBuilder


class HttpServer:
    def __init__(self):
        self.SERVER_HOST = '0.0.0.0'
        self.SERVER_PORT = 8000
        self.STATIC_DATA_FOLDER = 'static'

        self.SUPPORTED_CONTENT_TYPES = startup.get_supported_content_types() 
        self.sock = None
        self.controller_map = startup.build_controller_map()
        self.static_content_provider = startup.get_static_content_provider()

    def build_server(self):
        """Build a socket of IPV4 and TCP."""
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.bind((self.SERVER_HOST, self.SERVER_PORT))
        sock.listen(100)
        print("Server is listening on %s..." % self.SERVER_PORT)
        return sock
    
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

            response = None

            # Handle get request for static content
            if (parsed_request.path.startswith("/static") or parsed_request.path == "/favicon.ico") and parsed_request.method is HttpMethodType.GET:
                static_content_details = self.static_content_provider\
                                             .resolve(parsed_request.path.replace("/static", "", 1))

                if static_content_details is None:
                    response = responseBuilder.build(HttpStatus.NOT_FOUND, "Resource Not Found")
                else:
                    response = responseBuilder.build(HttpStatus.OK, static_content_details.content, {"Content-Type":static_content_details.content_type})
    
            else:
                routine = self.controller_map.fetch_endpoint(parsed_request.path)

                if routine is None:
                    response = responseBuilder.build(HttpStatus.NOT_FOUND, "Resource Not Found")
                else:
                    data = routine() 
                    serialized_data = json.dumps(data)
                    response = responseBuilder.build(HttpStatus.OK, serialized_data, {"Content-Type":"application/json"})


            client_connection.sendall(response)

    def shutdown(self):
        self.sock.close()


if __name__ == "__main__":
        server = HttpServer()

        try:
            server.run()
        except Exception as e:
            print(e.with_traceback)
            server.shutdown()
