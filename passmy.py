import random

def generate_password():
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input("How many symbols would you like?\n"))
    nr_numbers = int(input("How many numbers would you like?\n"))

    password_list = []

    for char in range(nr_letters):
        password_list.append(random.choice(letters))

    for char in range(nr_symbols):
        password_list.append(random.choice(numbers))

    for char in range(nr_numbers):
        password_list.append(random.choice(symbols))

    random.shuffle(password_list)

    password = "".join(password_list)
    print(f"Your random password is: {password}")

def check_password_strength(password):
    # Define criteria for password strength
    length_ok = len(password) >= 8
    has_uppercase = any(char.isupper() for char in password)
    has_lowercase = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in '!@#$%^&*()_+-=[]{}|;:,.<>?/~' for char in password)

    # Check if all criteria are met
    if length_ok and has_uppercase and has_lowercase and has_digit and has_symbol:
        print("The password is strong.")
    else:
        print("The password is weak. Please make sure it contains at least 8 characters, including uppercase and lowercase letters, numbers, and symbols.")


print(r"""
_______  _______  _______  _______     _______          
(  ____ )(  ___  )(  ____ \(  ____ \   (       )|\     /|
| (    )|| (   ) || (    \/| (    \/   | () () |( \   / )
| (____)|| (___) || (_____ | (_____    | || || | \ (_) / 
|  _____)|  ___  |(_____  )(_____  )   | |(_)| |  \   /  
| (      | (   ) |      ) |      ) |   | |   | |   ) (   
| )      | )   ( |/\____) |/\____) | _ | )   ( |   | |   
|/       |/     \|\_______)\_______)(_)|/     \|   \_/   
                                                         
""")

option = input(r"""
1) Generate Passwords
2) Password Strength Checker

Choose an option >> """)

if option == '1':
    generate_password()
elif option == '2':
    password = input("Enter the password: ")
    check_password_strength(password)
else:
    print("Invalid option.")
