from prac_09.taxi import Taxi


def main():
    test_vehicle = Taxi(name="Prius 1", fuel=100, price_per_km=1.23)
    test_vehicle.drive(40)
    print(test_vehicle, test_vehicle.get_fare())
    test_vehicle.start_fare()
    test_vehicle.drive(100)
    print(test_vehicle, test_vehicle.get_fare())


main()
