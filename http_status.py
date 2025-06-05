class StatusCode:
    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message

    def __str__(self):
        return str(self.code) + " " + self.message


class HttpStatus:
    OK = StatusCode(200, "OK")
    NOT_FOUND = StatusCode(404, "NOT FOUND")
    BAD_REQUEST = StatusCode(400, "BAD REQUEST")
    INTERNAL_SERVER_ERROR = StatusCode(500, "INTERNAL SERVER ERROR")

