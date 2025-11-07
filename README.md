# User Registration & Login System

A **Python command-line application** for registering users, logging in, and recovering passwords. **Passwords are encrypted using a Caesar cipher** and stored in a text file.

---

## Features

- **Register:** Create a new user account
- **Login:** Authenticate with user ID and password
- **Recover Password:** Retrieve your original password
- **Menu interface:** Easy, interactive CLI

---

## How It Works

- **Caesar cipher encryption**  
  - Alphabet characters are shifted by 3
  - Digits and symbols are also shifted for extra obfuscation

- **User storage**  
  - Credentials saved in `users.txt`  
  - Format: `user_id,encrypted_password`

---

## Usage

1. **Save code to a file**, e.g., `user_system.py`
2. **Run the script:** `python user_system.py`
3. **Follow the menu prompts:**
- Register a new account
- Login with existing credentials
- Recover a forgotten password
- Exit the program

---

## Code Structure

- `caesar_encrypt(text, shift)` - Encrypts passwords
- `caesar_decrypt(text, shift)` - Decrypts encrypted passwords
- `save_user(user_id, encrypted_password)` - Writes credentials to file
- `load_users()` - Loads credentials from file
- `register()` - Adds a new user
- `login()` - Authenticates user credentials
- `recover_password()` - Shows original password
- `main()` - Menu loop

---

## Notes

- Uses a **fixed shift key (3)** for encryption.
- Not secure for real-world use—**for learning/demo only**.
- Creates `users.txt` in the same folder as your script.

---

## License

**Educational use only.**
