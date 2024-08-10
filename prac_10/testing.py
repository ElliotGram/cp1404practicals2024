"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return ' '.join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    test_car = Car()
    assert test_car._odometer == 0, "Car does not set odometer correctly"

    # Testing fuel setting in Car
    assert test_car.fuel == 0, "Car does not set default fuel correctly"
    test_car = Car(fuel=10)
    assert test_car.fuel == 10, "Car does not set provided fuel correctly"


run_tests()


# (PyCharm may see your >>> doctest comments and run doctests anyway.)
doctest.testmod()


# (don't change the tests, change the function!)


def format_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital and ending with a single full stop.
    >>> format_sentence('hello')
    'Hello.'
    >>> format_sentence('It is an ex parrot.')
    'It is an ex parrot.'
    >>> format_sentence('this is a test')
    'This is a test.'
    """
    if not phrase:
        return '.'

    phrase = phrase.strip().capitalize()
    if not phrase.endswith('.'):
        phrase += '.'
    return phrase
