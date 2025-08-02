from cryptography.fernet import Fernet 
import os 
import json 

KEY_FILE = "secret.key"
DATA_FILE = "credentials.json.encrypted"


def generate_key():
    key = Fernet.generate_key()
    with open(KEY_FILE, "wb") as key_file:
        key_file.write(key)

def load_key():
    if not os.path.exists(KEY_FILE):
        print("[!] No key found. Generating a new one...")
        generate_key()
    with open(KEY_FILE, "rb") as f:
        return f.read()

def encrypt_data(data, key):
    f = Fernet(key)
    return f.encrypt(data.encode())

def decrypt_data(encrypted_data, key):
    f = Fernet(key)
    return f.decrypt(encrypted_data).decode()

def save_credentials(credentials, key):
    data_json = json.dumps(credentials)
    encrypted = encrypt_data(data_json, key)
    with open(DATA_FILE, "wb") as file:
        file.write(encrypted)

def load_credentials(key):
    if not os.path.exists(DATA_FILE):
        return {}
    with open(DATA_FILE, "rb") as file:
        encrypted = file.read()
    try:
        data_json = decrypt_data(encrypted, key)
        return json.loads(data_json)
    except Exception as e:
        print("[!] Failed to decrypt credentials.")
        return {}

def add_credential(credentials):
    site = input("Site  name: ").strip()
    username = input("Username: ").strip()
    password = input("Password: ").strip()
    credentials[site] = {"username": username, "password":password}
    print("[+] Credential added.")

def get_credential(credentials):
    site = input("Enter site name to retrieve: ").strip()
    if site in credentials:
        print("\n--- Credentials ---")
        print(f"Site: {site}")
        print(f"Username: {credentials[site]['username']}")
        print(f"Password: {credentials[site]['password']}")
        print("-------------------\n")
    else:
        print("[!] Site not found.")

def show_menu():
    print("\n== Password Manager ==")
    print("1. Add credential")
    print("2. Get credential")
    print("3.Exit")

if __name__ == "__main__":
    key = load_key()
    creds = load_credentials(key)
    
    while True:
        show_menu()
        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_credential(creds)
            save_credentials(creds, key)
        elif choice == "2":
            get_credential(creds)
        elif choice == "3":
            print("Goodbye! 🔒")
            break
        else:
            print("Invalid option. Try again.")







