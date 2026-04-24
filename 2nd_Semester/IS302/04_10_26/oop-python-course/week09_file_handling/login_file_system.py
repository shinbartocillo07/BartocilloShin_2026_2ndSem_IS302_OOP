def register_():
    username_SGB = input("Enter username: ")
    password_SGB = input("Enter password: ")
    with open("users.txt", "a") as file_SGB:
        file_SGB.write(username_SGB + "," + password_SGB + "\n")
    print("Registration successful!")

def login_SGB():
    username_SGB = input("Enter username: ")
    password_SGB = input("Enter password: ")
    try:
        with open("users.txt", "r") as file_SGB:
            for line_SGB in file_SGB:
                stored_user_SGB, stored_pass_SGB = line_SGB.strip().split(",")
                if username_SGB == stored_user_SGB and password_SGB == stored_pass_SGB:
                    print("Login successful!")
                    return
        print("Invalid credentials!")
    except FileNotFoundError:
        print("No users registered yet!")

def main_SGB():
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Exit")
        choice_SGB = input("Enter choice: ")
        
        if choice_SGB == "1":
            register_SGB()
        elif choice_SGB == "2":
            login_SGB()
        elif choice_SGB == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")

main_SGB()