from admin import Admin


# Food class for obj
class FoodItem:
    def __init__(self, food_id, name, price, quantity):
        self.food_id = food_id
        self.name = name
        self.price = price
        self.quantity = quantity


# main class
class Restaurant:
    def __init__(self, name):
        self.name = name
        self.food_items = []
        self.customers = []
        self.orders = []

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

# ---------------
# Menu for admin
# ---------------
    @staticmethod
    def admin_menu(restaurant):
        name = input("Enter your name: ")
        email = input("Enter your email: ")
        address = input("Enter your address")
        n_admin = Admin(name, email, address)
        print(f"Welcome {name}")
        while True:
            print("1. Add item"
                  "2. remove item"
                  "3. Create New customer"
                  "4. View all customer"
                  "5. remove Customer"
                  "6. Update item price"
                  "7. Exit.")
            choice = int(input("Enter your choice: "))

            match choice:
                case 1:
                    name = input("Enter item name: ")
                    price = input("Enter item price: ")
                    quantity = input("Enter item quantity: ")
                    n_admin.add_item(restaurant, name, price, quantity)
                case 2:
                    f_id = int(input("Please give the food id to remove: "))
                    n_admin.remove_item(restaurant, f_id)
                case 3:
                    name = input("Enter customer name: ")
                    email = input("Enter customer email: ")
                    address = input("Enter customer address")
                    n_admin.create_customer(restaurant, name, email, address)
                case 4:
                    n_admin.view_all_customers(restaurant)
                case 5:
                    c_id = int(input("Enter customer id you want to remove: "))
                    n_admin.remove_customer(restaurant, c_id)
                case 6:
                    f_id = int(input("Please enter food id: "))
                    update_price = int(input("Please enter new price: "))
                    n_admin.update_item_price(restaurant, f_id, update_price)
                case 7:
                    break

# ---------------
# Menu for customer
# ---------------
    def customer_menu(self, restaurant):
        c_name = input("Please enter your name: ")
        c_email = input("Please enter your email address: ")
        c_address = input("Please enter your address")
        customer = None
        for c_obj in self.customers:
            if c_obj.email == c_email and c_obj.name.lower() == c_name.lower():
                customer = c_obj
                break

        if customer is None:
            return
        print(f"Welcome {c_name}")

        # customer menu. ---> might need to apply while loop for the menu section
        while True:
            print("Please choose an option: "
                  "1. View food items."
                  "2. Order food."
                  "3. Check balance."
                  "4. View past orders."
                  "5. Add balance."
                  "6. Exit.")
            choice = int(input("Please enter your choice: "))

            match choice:
                case 1:
                    customer.view_menu(restaurant)
                case 2:
                    f_id = int(input("Please enter food id: "))
                    quant = int(input("Please enter quantity: "))
                    customer.place_order(restaurant, f_id, quant)
                case 3:
                    print(customer.check_balance())
                case 4:
                    customer.check_past_order()
                case 5:
                    amount = int(input("Please enter the amount to add: "))
                    customer.add_balance(amount)
                case 6:
                    break
