from user import User
from customer import Customer


# ---------------
# Admin access
# ---------------
class Admin(User):
    def __init__(self, name, email, address):
        super().__init__(name, email, address)

    # ---------------
    # manage customer accounts
    # ---------------
    @staticmethod
    def create_customer(restaurant, name, email, address):
        new_customer = Customer(len(restaurant.customers) + 1, name, email, address)
        restaurant.customers.append(new_customer)

    @staticmethod
    def view_all_customers(restaurant):
        print("\n---------------------------------------------\n"
              "Customer detail: "
              "Id \t Name \t Email \t Address\n"
              "---------------------------------------------")
        for customer in restaurant.customers:
            print(f"{customer.customer_id} \t"
                  f"{customer.name}\t"
                  f"{customer.email}\t"
                  f"{customer.address}\n")

    @staticmethod
    def remove_customer(restaurant, customer_id):
        for customer in restaurant.customers:
            if customer.customer_id == customer_id:
                restaurant.customers.remove(customer)
                break

    # ---------------
    # food item methods
    # ---------------
    @staticmethod
    def add_item(restaurant, f_name, f_price, f_quantity):
        # new_item = FoodItem(random.randint, f_name, f_price, f_quantity)
        restaurant.add_item(f_name, f_price, f_quantity)

    @staticmethod
    def remove_item(restaurant, food_id):
        restaurant.remove_item(food_id)

    @staticmethod
    def update_item_price(restaurant, food_id, update_price):
        restaurant.update_item_price(food_id, update_price)