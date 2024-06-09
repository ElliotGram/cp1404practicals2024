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
    # Check for at least one lowercase character
    if not has_lowercase(password):
        return False
    # Check for at least one uppercase character
    if not has_uppercase(password):
        return False
    # Check for at least one digit
    if not has_digit(password):
        return False
    # Check for special characters if required
    if IS_SPECIAL_CHARACTER_REQUIRED:
        if not has_special_character(password):
            return False
    return True

def has_lowercase(password):
    """Check if password contains at least one lowercase character."""
    return any(char.islower() for char in password)

def has_uppercase(password):
    """Check if password contains at least one uppercase character."""
    return any(char.isupper() for char in password)

def has_digit(password):
    """Check if password contains at least one digit."""
    return any(char.isdigit() for char in password)

def has_special_character(password):
    """Check if password contains at least one special character."""
    return any(char in SPECIAL_CHARACTERS for char in password)


main()