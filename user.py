from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address