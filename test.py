from abc import ABC, abstractmethod




class User(ABC):
   def __init__(self, name, email, address):
       self.name = name
       self.email = email
       self.address = address

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
             "---------------------------------------------\n")
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
       if len(restaurant.food_items) > 0:
           for food in restaurant.food_items:
               print("------------------------------------------\n"
                     "---------------- Food Menu ---------------\n"
                     "------------------------------------------\n")
               print(f"Id: {food.food_id} Name: {food.name} Price: {food.price} Available Quantity: {food.quantity}")
       else:
           print("Sorry no food item is available.")


   def place_order(self, restaurant, food_id, quantity):
       for food in restaurant.food_items:
           if food.food_id == food_id:
               if food.quantity >= quantity:
                   total = food.price * quantity
                   if self.wallet >= total:
                       #  confirming the order
                       self.wallet -= total
                       food.quantity -= quantity
                       print(f"-----------------------------\n"
                             f"Your order for  {food.name}, quantity: {quantity}, u_price: {food.price}, total: {total} has been confirmed."
                             f"\n-----------------------------")
                       self.orders.append(Order(self.customer_id, food.name, quantity, food.price, total))
                       return
                   else:
                       print("Insufficient Balance")
                       return
               else:
                   print("Insufficient Quantity")
                   return
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
       if len(self.food_items) > 0:
           for food in self.food_items:
               print(f"Id: {food.food_id} Name: {food.name} Price: {food.price} Available Quantity: {food.quantity}")
       else:
           print("Sorry no food item is available.")


   def add_item(self, name, price, quantity):
       new_item = FoodItem((len(self.food_items) + 1), name, price, quantity)
       print("Food item created")
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
       address = input("Enter your address: ")
       n_admin = Admin(name, email, address)
       print(f"Welcome {name}")
       print(f"Your restaurant obj is: {restaurant}")
       while True:
           print("1. Add item\n"
                 "2. remove item\n"
                 "3. Create New customer\n"
                 "4. View all customer\n"
                 "5. remove Customer\n"
                 "6. Update item price\n"
                 "7. Exit.")
           choice = int(input("Enter your choice: "))


           match choice:
               case 1:
                   name = input("Enter item name: ")
                   price = int(input("Enter item price: "))
                   quantity = int(input("Enter item quantity: "))
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
               case _:
                   print("Invalid input")


# ---------------
# Menu for customer
# ---------------
   def customer_menu(self, restaurant):
       c_name = input("Please enter your name: ")
       c_email = input("Please enter your email address: ")
       c_address = input("Please enter your address: ")
       customer = None
       # restaurant.customers.append(customer)
       for c_obj in self.customers:
           if c_obj.email == c_email:
               customer = c_obj
               break


       if customer is None:
           print("Wrong customer name or email. Please try different")
           return
       print(f"Welcome {c_name}")
       print(f"Welcome your restaurant obj is: {restaurant}")


       # customer menu
       while True:
           print("Please choose an option: \n"
                 "1. View food items.\n"
                 "2. Order food.\n"
                 "3. Check balance.\n"
                 "4. View past orders.\n"
                 "5. Add balance.\n"
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
from restaurant import Restaurant


# restaurant instance
restaurant = Restaurant("Test Restaurant")


while True:
   print("Login as user: ")
   print("1. Admin")
   print("2. Customer")
   print("3. Exit")
   user_type = int(input("Enter your user type: "))


   match user_type:
       case 1:
           # Admin access
           restaurant.admin_menu(restaurant)
       case 2:
           # customer access
           restaurant.customer_menu(restaurant)
       case 3:
           break