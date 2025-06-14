from typing import Callable
from controllers.user_controller import UserController
from request_parser import HttpMethodType


class ControllerMap:
    def __init__(self, user_controller: UserController):
        self.user_controller = user_controller

        self.controller_map = {
            "/users" : 
            [
                {
                    "method": HttpMethodType.GET,
                    "call": self.user_controller.get_user_list
                },

                {
                    "method": HttpMethodType.POST,
                    "call": self.user_controller.add_user
                },
            ]
        }

    def fetch_endpoint(self, key: str, method: HttpMethodType) -> Callable | None:
        for endpoint in self.controller_map.get(key):
            if endpoint["method"] is method:
                return endpoint["call"]
        return None
