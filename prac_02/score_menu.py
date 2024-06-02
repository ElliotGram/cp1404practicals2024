"""
CP1404/CP5632 - Practical
Elliot Gram
"""

MENU = "(G)et a valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    print(MENU)
    choice = input("What do you wish to do: ").upper()
    if choice == "G":
        get_valid_score()
    elif choice == "P":
        result = score_result()
        print(result)




def get_valid_score(score):
    score = float(input("Enter score(0-100): "))
    check_score(score)


def check_score(score):
    if 0 >= score or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))


def score_result(score):
    if score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


if __name__ == '__main__':
    main()
