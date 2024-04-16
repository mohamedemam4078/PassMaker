import random
import argparse

def generate_password(nr_letters, nr_symbols, nr_numbers):
    letters = [
        'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
        'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D',
        'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
        'T', 'U', 'V', 'W', 'X', 'Y', 'Z'
    ]
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    
    password_list = []

    for _ in range(nr_letters):
        password_list.append(random.choice(letters))

    for _ in range(nr_symbols):
        password_list.append(random.choice(numbers))

    for _ in range(nr_numbers):
        password_list.append(random.choice(symbols))

    random.shuffle(password_list)

    password = "".join(password_list)
    print(f"""
Your random password is: {password}""")

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
        input(r"""
              Press Enter To Exit""")
    else:
        print("The password is weak. Please make sure it contains at least 8 characters, including uppercase and lowercase letters, numbers, and symbols.")
        input(r"""
              Press Enter To Exit""")

def parse_args():
    parser = argparse.ArgumentParser(description="Password Tool")
    parser.add_argument("-g", "--generate", action="store_true", help="Generate a password")
    parser.add_argument("-c", "--check", action="store", help="Check the strength of a password")
    parser.add_argument("-l", "--letters", type=int, help="Number of letters in the generated password")
    parser.add_argument("-s", "--symbols", type=int, help="Number of symbols in the generated password")
    parser.add_argument("-n", "--numbers", type=int, help="Number of numbers in the generated password")
    return parser.parse_args()

def show_menu():
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

    print(r"""
1) Generate Passwords
2) Password Strength Checker
""")

def main():
    args = parse_args()

    if args.generate:
        if args.letters is None or args.symbols is None or args.numbers is None:
            print("Error: Please provide the number of letters, symbols, and numbers.")
        else:
            generate_password(args.letters, args.symbols, args.numbers)
    elif args.check:
        check_password_strength(args.check)
    else:
        show_menu()
        option = input("Choose an option >> ")
        if option == '1':
            nr_letters = int(input(r"""
How many letters would you like in your password? """))
            nr_symbols = int(input(r"""
How many symbols would you like? """))
            nr_numbers = int(input(r"""
How many numbers would you like? """))
            generate_password(nr_letters, nr_symbols, nr_numbers)
        elif option == '2':
            password = input(r"""
Enter the password: """)
            check_password_strength(password)
        else:
            print(r"""
Invalid option.""")

if __name__ == "__main__":
    main()
