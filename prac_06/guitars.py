"""CP1404/CP5632 Practical - Basic testing for Guitar class"""
from prac_06.guitar import Guitar


def main():
    guitars = []
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        name = input("Name: ")

    if guitars:
        print("These are my guitars:")
        for guitar in guitars:
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = " (vintage)"
            print(guitar, vintage_string)

    else:
        print("No guitars")


main()
