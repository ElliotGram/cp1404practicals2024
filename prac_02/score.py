"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""


def main():
    score = float(input("Enter score: "))
    check_score(score)
    score_result(score)


def check_score(score):
    if 0 >= score or score > 100:
        print("Invalid score")
        score = float(input("Enter score: "))


def score_result(score):
    if score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


if __name__ == '__main__':
    main()
