from abc import ABC, abstractmethod
from restaurant import FoodItem


class User(ABC):
    def __init__(self, name, email, address):
        self.name = name
        self.email = email
        self.address = address