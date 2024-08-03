from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    test_vehicle = SilverServiceTaxi(name="Lambo", fuel=100, price_per_km=1.23, fanciness=100)
    test_vehicle.drive(40)
    print(test_vehicle, test_vehicle.get_fare())


main()
