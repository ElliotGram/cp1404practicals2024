from prac_09.taxi import Taxi


class SilverServiceTaxi(Taxi):
    flagfall = 4.50

    def __init__(self, name, fuel, price_per_km, fanciness):
        """Initialise a SilverServiceTaxi instance."""
        super().__init__(name, fuel, price_per_km)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        """Return the price for the taxi trip including flagfall."""
        return super().get_fare() + SilverServiceTaxi.flagfall

    def __str__(self):
        """Return a string like a Taxi but with the flagfall fee included."""
        return (f"{super().__str__()} plus flagfall of ${SilverServiceTaxi.flagfall:.2f}")
