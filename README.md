#Solvek-Cyber-sec
A collection of cybersecurity-related scripts built during my learning journey.

---

## 📁 Projects

### 1. Password Validator
- 📄 password_validator.py
- Checks if a password meets security rules (length, digits, symbols, digit sum)

## 📖 About this script

This password validator was originally provided by ChatGPT based on rules discussed in CS50’s Lecture 0. 

Instead of copy-pasting it, I **typed the entire code manually in my Linux VM** and spent over 25 iterations debugging and fixing syntax/logic issues myself. That hands-on fixing helped me understand:
- String manipulation
- Input validation
- Logical conditions

I didn’t create the core idea from scratch, but **fixing and analyzing the errors myself** gave me a much deeper understanding than just copy-pasting would have.

### 2. Brute Force Password Cracker 
📄 brute_force_demo.py
Demonstrates a brute force attack by using all possible character combinations until a target is matched. It is a great way to demonstrate and understand how insecure a short password can be. 


### 3. File Encryptor

A simpe Python script to encrypt and decrypt files using Fernet symmetric encryption.

## Features 
- Generates and stores encrytion key
- Encrypts and file into ".encrypted" format
- Decrypts back into ".decrypted"
- easy to use
## Usage 
1. Place a txt file ("example.txt") in the directory.
2. Run "python3 encrypt_decrypt.py"
3. check for "encrypted" and "decrypted" files created

## warning 
DO NOT UPLOAD YOU "SECRET.KEY' file anywhere. This key could decrypt you files.

## License 
MIT
