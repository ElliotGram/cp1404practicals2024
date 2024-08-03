from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi


def print_taxis(taxis):
    """Print the list of available taxis."""
    print("Taxis available:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")


def choose_taxi(taxis):
    """Prompt user to choose a taxi and return the selected taxi."""
    try:
        choice = int(input("Choose taxi: "))
        if 0 <= choice < len(taxis):
            return taxis[choice]
        else:
            print("Invalid taxi choice")
            return None
    except ValueError:
        print("Invalid taxi choice")
        return None

def drive_taxi(current_taxi):
    """Prompt user to input distance and drive the selected taxi."""
    try:
        distance = float(input("Drive how far? "))
        if distance < 0:
            print("Distance cannot be negative.")
            return
        cost = current_taxi.drive(distance)
        fare = current_taxi.get_fare()
        print(f"Your {current_taxi.name} trip cost you ${fare:.2f}")
        return fare
    except ValueError:
        print("Invalid distance input")

def main():
    taxis = [
        Taxi("Prius", 100, 1.23),
        SilverServiceTaxi("Limo", 100, 2.00, 1.5),
        SilverServiceTaxi("Hummer", 200, 4.00, 2.0)
    ]

    current_taxi = None
    total_bill = 0.0

    user_input = ""
    while user_input != 'q':
        print("Let's drive!")
        print("q)uit, c)hoose taxi, d)rive")
        user_input = input(">>> ").lower()

        if user_input == 'c':
            print_taxis(taxis)
            current_taxi = choose_taxi(taxis)
            if current_taxi:
                print(f"Current taxi: {current_taxi.name}")
            print(f"Bill to date: ${total_bill:.2f}")
        elif user_input == 'd':
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                fare = drive_taxi(current_taxi)
                if fare is not None:
                    total_bill += fare
                    print(f"Bill to date: ${total_bill:.2f}")
        elif user_input != 'q':
            print("Invalid option")

    print(f"Total trip cost: ${total_bill:.2f}")
    print("Taxis are now:")
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

if __name__ == "__main__":
    main()