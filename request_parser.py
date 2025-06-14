import logging
import json
from enum import Enum

logging.basicConfig(level=logging.INFO)

class HttpMethodType(Enum):
    GET = 1
    POST = 2
    PUT = 3
    DELETE = 4

 
class HttpRequest:
    def __init__(self, method_type: HttpMethodType, path: str, protocol: str, headers:dict, payload=None):
        self.method = method_type
        self.path = path
        self.payload = payload
        self.protocol = protocol
        self.headers = headers

    def __str__(self):
        return f"""
            METHOD: {self.method}
            PATH: {self.path}
            PROTOCOL: {self.protocol}
            HEADERS: {self.headers}\n\n
            PAYLOAD: {self.payload}
        """


class RequestParser():
    @staticmethod
    def parse(request:str) -> HttpRequest:
        """
        Parses a request and consisely seperates out different part of a user request.

        Args:
            request (str): 
                Request text given by client, typically as a result of .recv() 
                call on connection object
        """
        headers = {}
        request_parts = {}

        request_lines = request.split("\n")    

        for i in range(len(request_lines)):
            line = request_lines[i]

            if line.strip() == '':
                break

            if i == 0:
                method, path, protocol = line.split()

                if method == "GET":
                    request_parts["method"] = HttpMethodType.GET

                elif method == "POST":
                    request_parts["method"] = HttpMethodType.POST

                elif method == "PUT":
                    request_parts["method"] = HttpMethodType.PUT

                elif method == "DELETE":
                    request_parts["method"] = HttpMethodType.DELETE


                request_parts["path"] = path
                request_parts["http_version"] = protocol.split("/")[1]

                logging.debug("request parts:\n", request_parts)

                continue

            # seperate key and value from headers
            key = ""
            pos = 0

            while (pos < len(line) and line[pos] != ":"):
                key += line[pos]
                pos += 1

            value = line[pos+1:].strip()

            headers[key] = value

        json_payload = None

        if method == "POST" or method == "PUT":
            raw_payload = ''.join(request_lines[i:])
            json_payload = json.loads(raw_payload)

        request_object = HttpRequest(
                request_parts["method"], 
                request_parts["path"], 
                request_parts["http_version"],
                headers,
                json_payload
            )

        return request_object

