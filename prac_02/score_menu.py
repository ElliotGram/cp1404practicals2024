"""
CP1404/CP5632 - Practical
Elliot Gram
"""


def main():
    score = float(input("Enter score: "))
    check_score(score)
    result = score_result(score)
    print(result)


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
