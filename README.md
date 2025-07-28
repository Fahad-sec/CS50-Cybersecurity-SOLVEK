import  string

def is_valid_password(password):
    if len(password) < 8:
        return "password too short> must be at least 8 characters."

    has_number =any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)

    if not has_number:
        return "password must contain at least one number."

    if not has_symbol:
        return "password must contain at least one symbol."

    digit_sum = sum(int(char) for char in password if char.isdigit())
    if digit_sum != 25:
        return "digits in password must add up to 25."

    return "password is valid"
    

if __name__ ==  "__main__":
    password = input ("enter a password to validate: ")
    result = is_valid_password(password)
    print(result)
