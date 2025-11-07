def caesar_encrypt(text, shift):
    encrypted = ""
    for char in text:
        if char.isalpha():
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + shift) % 26 + base)
        elif char.isdigit():
            encrypted += str((int(char) + shift) % 10)
        else:
            encrypted += chr((ord(char) + shift) % 128)
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
            decrypted += chr((ord(char) - shift) % 128)
    return decrypted

def save_user(user_id, encrypted_password):
    with open("users.txt", "a") as file:
        file.write(f"{user_id},{encrypted_password}\n")

def load_users():
    users = {}
    try:
        with open("users.txt", "r") as file:
            for line in file:
                uid, pwd = line.strip().split(",")
                users[uid] = pwd
    except FileNotFoundError:
        pass
    return users

def register():
    users = load_users()
    while True:
        user_id = input("Enter a new user ID: ")
        if user_id in users:
            print("User ID already exists. Try another.")
        else:
            break
    password = input("Enter a password: ")
    shift_key = 3  # fixed simple key for example
    encrypted_password = caesar_encrypt(password, shift_key)
    save_user(user_id, encrypted_password)
    print(f"User {user_id} registered successfully.\n")

def login():
    users = load_users()
    user_id = input("Enter your user ID: ")
    if user_id not in users:
        print("User ID not found.\n")
        return
    password = input("Enter your password: ")
    shift_key = 3
    encrypted_password = caesar_encrypt(password, shift_key)
    if users[user_id] == encrypted_password:
        print("Login successful!\n")
    else:
        print("Incorrect password.\n")

def recover_password():
    users = load_users()
    user_id = input("Enter your user ID to recover password: ")
    if user_id not in users:
        print("User ID not found.\n")
        return
    shift_key = 3
    decrypted_password = caesar_decrypt(users[user_id], shift_key)
    print(f"Your password is: {decrypted_password}\n")

def main():
    while True:
        print("Menu:")
        print("1. Register")
        print("2. Login")
        print("3. Recover Password")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")
        if choice == '1':
            register()
        elif choice == '2':
            login()
        elif choice == '3':
            recover_password()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.\n")

if __name__ == "__main__":
    main()
