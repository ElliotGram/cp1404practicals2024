import random

# Printing a random integer between 5 and 20 (inclusive)
print(random.randint(5, 20))  # line 1
# Smallest: 5, Largest: 20

# Printing a random number from the range 3 to 9 (inclusive), skipping by 2
print(random.randrange(3, 10, 2))  # line 2
# Smallest: 3, Largest: 9
# No, line 2 could not produce a 4 since it skips by 2.

# Printing a random floating-point number between 2.5 and 5.5
print(random.uniform(2.5, 5.5))  # line 3
# Smallest: 2.5, Largest: 5.5
