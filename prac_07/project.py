"""CP1404/CP5632 Practical - Guitar Class"""
CURRENT_YEAR = 2024
VINTAGE_AGE = 50


class Project:
    """A class to represent a Guitar object."""

    def __init__(self, name="", year=0, arithmetic_sequence="", cost=0):
        """Initialize a Project instance."""
        self.name = name
        self.year = year
        self.arithmetic_sequence = arithmetic_sequence
        self.cost = cost

    def __str__(self):
        """Return a string representation of the Project object."""
        return f"{self.name}, {self.year}: ${self.cost:,.2f}"

    def get_age(self):
        """Return the age of the Project."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Return True if the Guitar is considered vintage, False otherwise."""
        return self.get_age() >= VINTAGE_AGE
