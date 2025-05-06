import random

def main():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    print("Simple password generator (shuffled version).")
    nr_of_letters = int(input("Desired number of letters in your password:\n"))
    nr_of_symbols = int(input(f"Desired number of symbols in your password:\n"))
    nr_of_numbers = int(input(f"Desired number of numbers in your password:\n"))

    letters_part = [random.choice(letters) for i in range(nr_of_letters)]
    symbols_part = [random.choice(symbols) for i in range(nr_of_symbols)]
    numbers_part = [random.choice(numbers) for i in range(nr_of_numbers)]

    combined_password = letters_part + symbols_part + numbers_part

    random.shuffle(combined_password)
    password = "".join(combined_password)
    print(f"Your password is: {password}")


if __name__ == "__main__":
    main()