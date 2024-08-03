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

function main:
    Create taxis
    Set current_taxi to None
    Set total_bill to 0

    Repeat until user_input is 'q':
        Show menu options
        Get user_input

        if user_input is 'c':
            Show taxis
            Set current_taxi based on choice

        else if user_input is 'd':
            if current_taxi is None:
                Show message to choose taxi first
            else:
                Get distance
                Calculate cost
                Update total_bill

        else:
            Show invalid option message

    Show total_bill
    Show final state of taxis
