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

    @staticmethod
    def place_order(restaurant, food_id, quantity):
        for food in restaurant.food_items:
            if food.food_id == food_id and food.quantity >= quantity:
                food.quantity -= quantity
                print("Successfully placed the order")
                return
        print("Order not successful. Invalid ID or quantity were given")

