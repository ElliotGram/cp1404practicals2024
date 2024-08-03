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
