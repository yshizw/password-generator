# Password Generator

A simple Python password generator that creates random passwords based on user specifications. The length and types of characters (letters, numbers, symbols) are customizable, generating a unique password every time.


##Features

- Basic: Generates a basic password with customizable length and content. The order is fixed (letters, numbers, symbols).
- Shuffled: Generates a password where the content is shuffled using random.shuffle for a more secure, randomized password.
- Customizable password length.
- Options include:
- Uppercase and lowercase letters (randomized)
- Numbers
- Special characters (e.g., !, @, #, etc.)
- Generates a random password every time the script runs.


##How It Works

The script uses the random module to select random characters from predefined lists of uppercase and lowercase letters, numbers, and special symbols. The length and content of the password are customizable based on the user's input.
