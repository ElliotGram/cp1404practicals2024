"""CP1404/CP5632 Practical - Basic testing for Guitar class"""
from prac_06.guitar import Guitar


def main():
    fender = Guitar("FenderBender", 1999, 459)
    print(fender)

    print(f"{fender.name} Expected 25. Got {fender.get_age()}")


main()
