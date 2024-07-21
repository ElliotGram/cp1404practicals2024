"""CP1404/CP5632 Practical - Basic testing for Guitar class"""
from prac_07.guitar import Guitar


def main():
    guitars = []

    get_guitar_information(guitars)

    display_guitar(guitars)


def get_guitar_information(guitars):
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        guitar_to_add = Guitar(name, year, cost)
        guitars.append(guitar_to_add)
        print(guitar_to_add, "added.")
        name = input("Name: ")

    return guitars


def display_guitar(guitars):
    if guitars:
        print("These are my guitars:")
        for i, guitar in enumerate(guitars, 1):
            vintage_string = ""
            if guitar.is_vintage():
                vintage_string = " (vintage)"
            # Note the use of the format method and numbered placeholders
            print("Guitar {0}: {1.name:>20} ({1.year}), worth ${1.cost:10,.2f}{2}".format(i, guitar, vintage_string))

    else:
        print("No guitars")


main()
