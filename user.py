from abc import ABC, abstractmethod


class User(ABC):
    def __init__(self, name, email, address, nid):
        self.name = name
        self.email = email
        self.address = address
        self.nid = nid


class Customer(User):
    def __init__(self, name, email, address, nid):
        super().__init__(name, email, address, nid)
