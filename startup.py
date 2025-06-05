import json

from controllers.map import ControllerMap
from controllers.user_controller import UserController
from static_content_provider import StaticContentProvider

def get_static_content_provider() -> StaticContentProvider:
    return StaticContentProvider(
        static_data_folder='static', 
        content_types= get_supported_content_types() 
        )

def get_supported_content_types():
    return load_config('content_types.json')

def load_config(filename: str):
    return json.load(open(filename))

def build_controller_map(): 
    return ControllerMap(
        user_controller=UserController()
        )