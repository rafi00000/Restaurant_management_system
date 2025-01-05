
class FoodItem:
    def __init__(self, food_id, name, price, quantity):
        self.id = food_id
        self.name = name
        self.price = price
        self.quantity = quantity


class Restaurant:
    def __init__(self, name):
        self.name = name
        self.food_item = []
        self.customer = []

    def add_item(self, name, price, quantity):
        new_item = FoodItem((len(self.food_item) + 1), name, price, quantity)
        self.food_item.append(new_item)

    def remove_item(self, food_id):
        for food in self.food_item:
            if food.id.lower() == food_id:
