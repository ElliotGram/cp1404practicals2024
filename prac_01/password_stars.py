"""
Password into stars
"""

import random

minimum_length = random.randint(1, 10)


def get_password():
    password = input("Enter a password: ")
    return password


def check_length(password):
    while len(password) < minimum_length:
        print("Password is too short. Minimum length is", minimum_length)
        password = get_password()
    print("*" * len(password))


password = get_password()
check_length(password)
