"""
CP1404/CP5632 - Practical
Elliot Gram
"""

MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    score = None
    print(MENU)
    choice = input("What do you wish to do: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            if score is not None:
                result = score_result(score)
                print(result)
            else:
                print("Score has not been set yet.")
        elif choice == "S":
            if score is not None:
                show_stars(score)
            else:
                print("Score has not been set yet.")
        else:
            print("Invalid choice")
        print(MENU)
        choice = input("What do you wish to do: ").upper()
    print("Goodbye!")


def get_valid_score():
    while True:
        try:
            score = float(input("Enter score(0-100): "))
            if 0 <= score <= 100:
                return score
            else:
                print("Invalid score")
        except ValueError:
            print("Invalid input")


def score_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def show_stars(score):
    print("*" * int(score))


if __name__ == '__main__':
    main()
