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
📄 encrypt_decrypt.py

This script was written as part of my journey learning file encryption with Python and the cryptography module. It encrypts and decrypts files using Fernet symmetric encryption. It's a simple demo for personal understanding, not meant for production use.

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


### 4. Password Manager
-📄 password_manager.py

This is a simple script written as a part of the CS-50 Cybersec course and is inspired by lecture 1. The script uses cryptography and Fernet to encrypt credentials by using a key and saves it to a file, the creentials are given by a user, this script can also decrypt those credentials given if you choose that option uppon running the command.

## Output of the Command
python3 password_manager.py

== Password Manager ==
1. Add credential
   
3. Get credential

3. Exit

Choose an option:

