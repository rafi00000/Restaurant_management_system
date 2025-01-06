from user import Admin, Customer
from restaurant import Restaurant

while True:
    print("Login as user: ")
    print("1. Admin")
    print("2. Customer")
    print("3. Exit")
    user_type = int(input("Enter your user type: "))

    # restaurant instance
    res = Restaurant("Test Restaurant")

    match user_type:
        case 1:
            # Admin access
            print(f"Welcome Admin")
            print("1. Add item"
                  "2. remove item"
                  "3. ")
            pass
        case 2:
            pass
            # customer access
        case 3:
            break