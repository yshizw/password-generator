import random

def main():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Simple password generator (basic version).")
    nr_of_letters = int(input("Desired number of letters in your password:\n"))
    nr_of_symbols = int(input(f"Desired number of symbols in your password:\n"))
    nr_of_numbers = int(input(f"Desired number of numbers in your password:\n"))

    password = ""
    #range(1, nr_letters +1) OU range(0, nr_letters)
    for i in range(0, nr_of_letters):
        letter_password = random.choice(letters)
        password += letter_password
    for i in range(0, nr_of_symbols):
        symbol_password = random.choice(symbols)
        password += symbol_password
    for i in range(0, nr_of_numbers):
        number_password = random.choice(numbers)
        password += number_password
    print(f"Your password is: {password}")


if __name__ == "__main__":
    main()