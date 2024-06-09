"""
CP1404/CP5632 - Practical
Password checker "skeleton" code to help you get started
"""

MIN_LENGTH = 2
MAX_LENGTH = 6
IS_SPECIAL_CHARACTER_REQUIRED = False
SPECIAL_CHARACTERS = "!@#$%^&*()_-=+`~,./'[]<>?{}|\\"


def main():
    """Program to get and check a user's password."""
    print("Please enter a valid password")
    print(f"Your password must be between {MIN_LENGTH} and {MAX_LENGTH} characters, and contain:")
    print("\t1 or more uppercase characters")
    print("\t1 or more lowercase characters")
    print("\t1 or more numbers")
    if IS_SPECIAL_CHARACTER_REQUIRED:
        print("\tand 1 or more special characters: ", SPECIAL_CHARACTERS)
    password = input("> ")
    while not is_valid_password(password):
        print("Invalid password!")
        password = input("> ")
    print(f"Your {len(password)}-character password is valid: {password}")


def is_valid_password(password):
    """Determine if the provided password is valid."""
    # Check if length is within the specified range
    if not MIN_LENGTH <= len(password) <= MAX_LENGTH:
        return False
    # Count lowercase characters
    number_of_lower = sum(1 for char in password if char.islower())
    if number_of_lower == 0:
        return False
    # Count uppercase characters
    number_of_upper = sum(1 for char in password if char.isupper())
    if number_of_upper == 0:
        return False
    # Count digits
    number_of_digits = sum(1 for char in password if char.isdigit())
    if number_of_digits == 0:
        return False
    # Check if special characters are required
    if IS_SPECIAL_CHARACTER_REQUIRED:
        number_of_special = sum(1 for char in password if char in SPECIAL_CHARACTERS)
        if number_of_special == 0:
            return False


main()