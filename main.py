

while True:
    print("Login as user: ")
    print("1. Admin")
    print("2. Customer")
    print("3. Exit")
    user_type = int(input("Enter your user type: "))

    match user_type:
        case 1:
            # Admin access
            pass
        case 2:
            pass
            # customer access
        case 3:
            break