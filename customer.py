from user import User


class Order:
    def __init__(self, customer_id, f_name, f_quant, f_price, f_total):
        self.customer_id = customer_id
        self.f_name = f_name
        self.f_quant = f_quant
        self.f_price = f_price
        self.f_total = f_total


class Customer(User):
    def __init__(self, customer_id, name, email, address):
        self.customer_id = customer_id
        self.wallet = 0
        self.orders = []
        super().__init__(name, email, address)

    @staticmethod
    def view_menu(restaurant):
        restaurant.view_items()

    def place_order(self, restaurant, food_id, quantity):
        for food in restaurant.food_items:
            if food.food_id == food_id:
                if food.quantity >= quantity:
                    total = food.price * quantity
                    if self.wallet >= total:
                        #  confirming the order
                        self.wallet -= total
                        food.quantity -= quantity
                        self.orders.append(Order(self.customer_id, food.name, food.quantity, food.price, total))
                        return
                    else:
                        print("Insufficient Balance")
                else:
                    print("Insufficient Quantity")
        print("Wrong food id")

    def check_balance(self):
        return self.wallet

    def add_balance(self, amount):
        if amount > 0:
            self.wallet += amount
        else:
            print("Invalid amount input")

    def check_past_order(self):
        for order in self.orders:
            print(f"F_Name: {order.f_name}, F_price: {order.f_price}, F_Quant: {order.f_quant}, Total: {order.f_total}")
