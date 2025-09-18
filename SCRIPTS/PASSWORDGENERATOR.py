import secrets
import random
import string

def gen_password(length=16):
    if length < 4:
        print("Password lenghth should be at least 4 to be strong.")
        length = 4

    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    password_chars= [
        secrets.choice(lowercase),
        secrets.choice(uppercase),
        secrets.choice(digits),
        secrets.choice(symbols)
    ]

    all_chars = lowercase + uppercase + digits + symbols
    remaining_length = length - 4
    if remaining_length >0:
        password_chars.extend(secrets.choice(all_chars) for _ in range(remaining_length))

    random.shuffle(password_chars)

    return ''.join(password_chars)

try:
    length_input = input("Enter desired password length (default 16): ")
    if not length_input:
        password_length = 16
    else:
        password_length = int(length_input)

    new_password = gen_password(password_length) 
    print(f"Generated password: {new_password}")
except ValueError:
    print("You need to enter a number") 
    