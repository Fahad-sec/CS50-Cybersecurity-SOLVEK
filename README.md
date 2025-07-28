"""
Solvek-cybersec
Course projects and labs for CS50’s Introduction to Cybersecurity.

WEEK 0 – Password Rule Validator:

- Must be at least 8 characters long
- Must contain at least one digit
- Must contain at least one symbol
- Digits in the password must add up to 25
"""
import string

def is_valid_password(password):
    if len(password) < 8:
        return "Password too short: must be at least 8 characters."

    has_number = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)

    if not has_number:
        return "Password must contain at least one number."

    if not has_symbol:
        return "Password must contain at least one symbol."

    digit_sum = sum(int(char) for char in password if char.isdigit())
    if digit_sum != 25:
        return f"Digits must add up to 25. Yours add up to {digit_sum}."

    return "Password is valid."

if __name__ == "__main__":
    password = input("Enter a password to validate: ")
    result = is_valid_password(password)
    print(result)


