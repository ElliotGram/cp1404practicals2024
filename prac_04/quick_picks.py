import random

# Constants
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_LINE = 6

def main():
    num_picks = int(input("How many quick picks? "))
    generate_quick_picks(num_picks)


def generate_quick_picks(num_picks):
    for _ in range(num_picks):
        # Generate a list of unique random numbers
        numbers = []
        while len(numbers) < NUMBERS_PER_LINE:
            new_number = random.randint(MIN_NUMBER, MAX_NUMBER)
            if new_number not in numbers:
                numbers.append(new_number)