# Write user's name to a file
name = input("Enter your name: ")
with open('name.txt', 'w') as file:
    file.write(name)
