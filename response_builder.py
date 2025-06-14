import json
from http_status import StatusCode

class HttpResponseBuilder:
    def __init__(self, http_version="1.0"):
        self.http_version = http_version

    def build(self, status_code: StatusCode, content: bytes | str, headers: dict = {}) -> str:
        if type(content) == str:
            content = content.encode()

        response = f"HTTP/{self.http_version} {str(status_code)}\n"

        for k, v in headers.items():
            response += (k + ":" + v + "\n")
        
        response += "\n"

        return response.encode() + content