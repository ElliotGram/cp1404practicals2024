"""CP1404/CP5632 Practical - Guitar Class"""
class Guitar:
    """Represent a guitar object."""
    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance"""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return a string representation of guitar name year and cost"""
        return f"{self.name}, {self.year}: {self.cost}"

    def get_age(self):
        """Return age of guitar"""
        age = CURRENT_YEAR - self.year
        return age

    def is_vintage(self):
        """Determines if guitar is vintage"""
        if self.year >= VINTAGE_AGE:
            return True
        else:
            return False
