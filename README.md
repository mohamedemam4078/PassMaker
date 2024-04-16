# PassMaker

PassMaker is a Python-based password generator and strength checker tool that allows you to generate strong passwords and check the strength of existing passwords.

## Features

- Generate random passwords with custom lengths and compositions of letters, symbols, and numbers.
- Check the strength of passwords based on criteria such as length, uppercase letters, lowercase letters, numbers, and symbols.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/mohamedemam4078/passmaker.git
    ```

2. Navigate to the project directory:

    ```bash
    cd passmaker
    ```

### Usage

#### Generating Passwords

To generate a password, use the following command:

```bash
python passmaker.py -g -l <number_of_letters> -s <number_of_symbols> -n <number_of_numbers>
```

Example:

```bash
python passmaker.py -g -l 8 -s 2 -n 2
```

This will generate a password with 8 letters, 2 symbols, and 2 numbers.

#### Checking Password Strength

To check the strength of a password, use the following command:

```bash
python passmaker.py -c <password>
```

Example:

```bash
python passmaker.py -c StrongPassword123!
```

This will check the strength of the password "StrongPassword123!".

## Contributing

Contributions are welcome! Please feel free to submit issues and pull requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
