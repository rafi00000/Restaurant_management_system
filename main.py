from restaurant import Restaurant

while True:
    print("Login as user: ")
    print("1. Admin")
    print("2. Customer")
    print("3. Exit")
    user_type = int(input("Enter your user type: "))

    # restaurant instance
    restaurant = Restaurant("Test Restaurant")

    match user_type:
        case 1:
            # Admin access
            restaurant.admin_menu(restaurant)
        case 2:
            # customer access
            restaurant.customer_menu(restaurant)
        case 3:
            break
