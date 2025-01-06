# Food class for obj
class FoodItem:
    def __init__(self, food_id, name, price, quantity):
        self.food_id = food_id
        self.name = name
        self.price = price
        self.quantity = quantity


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.food_items = []
        self.customers = []
        self.orders = {}

    # ------------------
    # manage restaurant menu
    # ------------------
    def view_one_item(self, food_id):
        for food in self.food_items:
            if food.food_id == food_id:
                print(f"Id: {food.food_id} Name: {food.name} Price: {food.price} Available Quantity: {food.quantity}")
                break

    def view_items(self):
        for food in self.food_items:
            print(f"Id: {food.food_id} Name: {food.name} Price: {food.price} Available Quantity: {food.quantity}")

    def add_item(self, name, price, quantity):
        new_item = FoodItem((len(self.food_items) + 1), name, price, quantity)
        self.food_items.append(new_item)

    def remove_item(self, food_id):
        for food in self.food_items:
            if food.food_id == food_id:
                self.food_items.remove(food)
                return
            print("Invalid Id")

    def update_item_price(self, food_id, update_price):
        for item in self.food_items:
            if item.food_id == food_id:
                item.price = update_price
            return
        print("Item not found")

    # ---------------
    # manage customer accounts
    # ---------------
    def customer_details(self, customer_id):
        for customer in self.customers:
            if customer.customer_id == customer_id:
                print(f"Name: {customer.name}, Email: {customer.email}, Address: {customer.address}, \n "
                      f"Wallet: {customer.wallet}")
                return
        print("Invalid Customer id. Not found")
