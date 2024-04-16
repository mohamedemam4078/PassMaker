# Pass.My

This Python script serves as a versatile tool for enhancing online security. It offers two essential functionalities:

1. **Password Generator**: Generate strong, random passwords tailored to your specifications, including length and character composition.

2. **Password Strength Checker**: Evaluate the strength of your existing passwords based on criteria such as length, presence of uppercase and lowercase letters, numbers, and symbols.

## Usage

1. **Generate Password**:
   - Use the command `-g` or `--generate` to generate a password.
   - Specify the number of letters, symbols, and numbers using `-l`, `-s`, and `-n` respectively.
   - Example: `python passmy.py -g -l 8 -s 2 -n 3`

2. **Check Password Strength**:
   - Use the command `-c` or `--check` followed by the password to check its strength.
   - Example: `python passmy.py -c mypassword123`

If no command-line arguments are provided, the script will display a menu screen allowing you to choose the desired option interactively.

## Contributions

Contributions and feedback are welcome! Feel free to fork the repository, make improvements, and submit pull requests.
