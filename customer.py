from user import User


class Customer(User):
    def __init__(self, customer_id, name, email, address):
        self.customer_id = customer_id
        self.wallet = 0
        self.orders = []
        super().__init__(name, email, address)

    @staticmethod
    def view_menu(restaurant):
        restaurant.view_items()
