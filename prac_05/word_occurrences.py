"""
Word Occurrences
Estimate: 20 minutes
Actual:   20 minutes
"""


def main():
    text = input("Enter a string: ")
    word_counts = count_word_occurrences(text)
    max_width = max(len(word) for word in word_counts.keys())
    for word in sorted(word_counts.keys()):
        count = word_counts[word]
        print(f"{word:>{max_width}} : {count}")


def count_word_occurrences(text):
    words = text.split()
    word_counts = {}
    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts


main()
