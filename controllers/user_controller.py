import json

class User:
    def __init__(self, name: str, age: int, city: str):
        self.name = name
        self.age = age
        self.city = city


class UserController:
    def __init__(self):
        self.db_path = "users.json"
        self.users = json.load(open(self.db_path, "r"))

    def get_user_list(self):
        return self.users

    def add_user(self, new_user: dict):
        self.users.append(new_user)
        json.dump(self.users, open(self.db_path, "w"), indent=4)