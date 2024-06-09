"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    - A ValueError will occur if the input provided for either the numerator or denominator cannot be converted to an integer.

2. When will a ZeroDivisionError occur?
    - A ZeroDivisionError will occur if the denominator provided by the user is 0.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    - Yes, we can change the code to handle the case where the denominator is 0 by asking the user to input a new denominator until it's not 0.

"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator (not zero): "))  # Ensure denominator is not zero
    while denominator == 0:  # Keep asking for denominator until it's not zero
        print("Denominator cannot be zero!")
        denominator = int(input("Enter the denominator (not zero): "))

    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
print("Finished.")
