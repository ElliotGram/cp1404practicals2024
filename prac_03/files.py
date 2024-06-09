# Write user's name to a file
name = input("Enter your name: ")
with open('name.txt', 'w') as file:
    file.write(name)

# Read name from file and print greeting
with open('name.txt', 'r') as file:
    name = file.read()
print(f"Hi {name}!")
