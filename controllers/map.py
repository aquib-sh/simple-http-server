from typing import Callable
from controllers.user_controller import UserController


class ControllerMap:
    def __init__(self, user_controller: UserController):
        self.user_controller = user_controller

        self.controller_map = {
            "/users" : self.user_controller.get_user_list
        }

    def fetch_endpoint(self, key: str) -> Callable | None:
        return self.controller_map.get(key)