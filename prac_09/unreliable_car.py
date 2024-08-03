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

