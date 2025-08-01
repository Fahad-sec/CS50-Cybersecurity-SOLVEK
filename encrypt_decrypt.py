from cryptography.fernet import Fernet 
import os 

def generate_key():
     key = Fernet.generate_key()
     with open("secret.key", "wb")as key_file:
        key_file.write(key)

def load_key():
    if not os.path.exists("secret.key"):
        print("[!] key not found. Generating a new one...")
        generate_key()
    return open("secret.key", "rb").read()

def encrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        data = file.read()
    encrypted = f.encrypt(data)
    with open(filename + ".encrypted", "wb") as file:
        file.write(encrypted)


def decrypt_file(filename, key):
    f = Fernet(key)
    with open(filename, "rb") as file:
        encrypted_data = file.read()
    decrypted = f.decrypt(encrypted_data)
    original_filename = filename.rsplit(".encrypted", 1)[0]
    with open(original_filename + ".decrypted", "wb") as file:
        file.write(decrypted)

if __name__ == "__main__":


    key = load_key()
    encrypt_file("example.txt", key)
    decrypt_file("example.txt.encrypted", key)
    print("[✓] File encryption complete: example.txt.encrypted")
    print("[✓] File decryption complete: example.txt.decrypted")

input("🎉 Done! Press Enter to exit...")

