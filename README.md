# Password-Encryption
def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        # Encrypt alphabets
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        # Encrypt digits
        elif char.isdigit():
            encrypted += str((int(char) + shift) % 10)
        # Encrypt symbols by ASCII shifting (within range 32 to 126 printable chars)
        else:
            new_code = ord(char) + shift
            if new_code > 126:
                new_code = 31 + (new_code - 126)
            encrypted += chr(new_code)
    return encrypted

def caesar_decrypt(text, shift):
    decrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            decrypted += chr((ord(char) - base - shift) % 26 + base)
        elif char.isdigit():
            decrypted += str((int(char) - shift) % 10)
        else:
            new_code = ord(char) - shift
            if new_code < 32:
                new_code = 127 - (32 - new_code)
            decrypted += chr(new_code)
    return decrypted

def save_users(users):
    # Save dictionary {user_id: {"password": encrypted_pwd, "shift": key}} to file
    with open("users_db.txt", "w") as f:
        for uid, data in users.items():
            line = f"{uid},{data['password']},{data['shift']}\n"
            f.write(line)

def load_users():
    users = {}
    try:
        with open("users_db.txt", "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                uid, encrypted_pwd, shift = line.split(",", 2)
                users[uid] = {"password": encrypted_pwd, "shift": int(shift)}
    except FileNotFoundError:
        # If file not found, return empty dict
        pass
    return users

def register_user(users):
    print("\n--- User Registration ---")
    while True:
        user_id = input("Enter your desired user ID: ").strip()
        if not user_id:
            print("User ID cannot be empty.")
            continue
        if user_id in users:
            print("User ID already exists. Choose something else.")
            continue
        break
    while True:
        password = input("Enter your password: ").strip()
        if len(password) < 4:
            print("Password should be at least 4 characters.")
        else:
            break
    while True:
        try:
            shift = int(input("Enter encryption key (1-25): "))
            if 1 <= shift <= 25:
                break
            else:
                print("Key must be between 1 and 25.")
        except ValueError:
            print("Invalid number.")
    encrypted_pwd = caesar_encrypt(password, shift)
    users[user_id] = {"password": encrypted_pwd, "shift": shift}
    save_users(users)
    print(f"User '{user_id}' registered successfully.")

def login_user(users):
    print("\n--- Login ---")
    user_id = input("Enter user ID: ").strip()
    if user_id not in users:
        print("User ID not found.")
        return
    password = input("Enter password: ").strip()
    data = users[user_id]
    decrypted_pwd = caesar_decrypt(data["password"], data["shift"])
    if password == decrypted_pwd:
        print(f"Welcome {user_id}! Login successful.")
        user_menu(users, user_id)
    else:
        print("Wrong password.")

def change_password(users, user_id):
    print("\n--- Change Password ---")
    current_pwd = input("Enter current password: ").strip()
    data = users[user_id]
    decrypted_pwd = caesar_decrypt(data["password"], data["shift"])
    if current_pwd != decrypted_pwd:
        print("Incorrect current password. Cannot change password.")
        return
    while True:
        new_pwd = input("Enter new password: ").strip()
        if len(new_pwd) < 4:
            print("Password must be at least 4 characters.")
        else:
            break
    while True:
        try:
            new_shift = int(input("Enter new encryption key (1-25): "))
            if 1 <= new_shift <= 25:
                break
            else:
                print("Key must be between 1 and 25.")
        except ValueError:
            print("Invalid number.")
    new_encrypted = caesar_encrypt(new_pwd, new_shift)
    users[user_id] = {"password": new_encrypted, "shift": new_shift}
    save_users(users)
    print("Password changed successfully.")

def recover_password(users):
    print("\n--- Recover Password ---")
    user_id = input("Enter your user ID: ").strip()
    if user_id not in users:
        print("User ID not found.")
        return
    data = users[user_id]
    decrypted_pwd = caesar_decrypt(data["password"], data["shift"])
    print(f"Password for user '{user_id}' is: {decrypted_pwd}")

def user_menu(users, user_id):
    while True:
        print(f"\n== User Menu ({user_id}) ==")
        print("1. Change Password")
        print("2. Logout")
        choice = input("Enter choice: ").strip()
        if choice == '1':
            change_password(users, user_id)
        elif choice == '2':
            print("Logging out...")
            break
        else:
            print("Invalid choice.")

def main_menu():
    users = load_users()
    while True:
        print("\n=== Main Menu ===")
        print("1. Register New User")
        print("2. Login")
        print("3. Recover Password")
        print("4. Exit")
        choice = input("Enter choice: ").strip()
        if choice == '1':
            register_user(users)
        elif choice == '2':
            login_user(users)
        elif choice == '3':
            recover_password(users)
        elif choice == '4':
            print("Exiting program. Goodbye.")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main_menu()
