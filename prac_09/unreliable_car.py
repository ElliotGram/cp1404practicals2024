import random
from prac_09.car import Car


class UnreliableCar(Car):
    """Represent an Unreliable Car object that inherits from Car."""

    def __init__(self, name, fuel, reliability):
        """Initialise an UnreliableCar instance.

        name: string, reference name for the car
        fuel: float, one unit of fuel drives one kilometre
        reliability: float, the percentage chance of the car actually driving
        """
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car a given distance based on its reliability.

        Only drive if a randomly generated number is less than the car's reliability.
        """
        if random.uniform(0, 100) < self.reliability:
            return super().drive(distance)
        return 0
