# Write user's name to a file
name = input("Enter your name: ")
with open('name.txt', 'w') as file:
    file.write(name)

# Read name from file and print greeting
with open('name.txt', 'r') as file:
    name = file.read()
print(f"Hi {name}!")

# Read first two numbers from file and print their sum
with open('numbers.txt', 'r') as file:
    number1 = int(file.readline())
    number2 = int(file.readline())
result = number1 + number2
print(f"The sum of the first two numbers is: {result}")

# Read and print total for all numbers in file
total = 0
with open('numbers.txt', 'r') as file:
    for line in file:
        total += int(line)
print(f"The total for all numbers in the file is: {total}")
