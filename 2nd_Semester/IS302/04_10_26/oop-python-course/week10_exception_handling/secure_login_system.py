def load_users(filepath="users.txt"):
    users_SGB = {}
    with open(filepath, "r") as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            parts = line.split(",")
            if len(parts) != 2:
                raise ValueError("Invalid user data format")
            username_SGB = parts[0].strip()
            password_SGB = parts[1].strip()
            users_SGB[username_SGB] = password_SGB
    return users_SGB


def main():
    try:
        users_SGB = load_users("users.txt")
    except FileNotFoundError:
        print("User credentials file not found.")
        return
    except ValueError as err:
        print("Error loading users:", err)
        return

    username_SGB = input("Enter username: ").strip()
    password_SGB = input("Enter password: ").strip()

    if not username_SGB or not password_SGB:
        print("Username and password cannot be empty.")
        return

    if username_SGB in users_SGB and users_SGB[username_SGB] == password_SGB:
        print("Login successful.")
    else:
        print("Login failed. Check username and password.")


if __name__ == "__main__":
    main()
