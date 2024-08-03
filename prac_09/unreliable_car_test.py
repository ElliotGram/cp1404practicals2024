from prac_09.unreliable_car import UnreliableCar


def main():
    test_vehicle = UnreliableCar(name="Prius 1", fuel=100, reliability=50)
    test_vehicle.drive(40)
    print(test_vehicle)


main()
