"""
CP1404/CP5632 Practical
Testing demo using assert and doctest
"""

import doctest
from Prac6.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return s * n


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
    # the test below should fail
    assert '-'.join(["hi", "hi"]) == "hi-hi"
    # print('passed')

    # 1. fix the repeat_string function above so that it passes the failing test
    # Hint: "-".join(["yo", "yo"] -> "yo-yo"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    test_car = Car()
    assert test_car._odometer == 0, "Car does not set odometer correctly"

    # 2. Wrote assert statements to show if Car sets the fuel correctly
    # Note that Car's __init__ function sets the fuel in one of two ways:
    # using the value passed in or the default
    # You should test both of these
    test_car = Car(fuel=10)
    assert test_car.fuel == 10
    # print('passed')
    test_car = Car()
    assert test_car.fuel == 0

    sentence = phrase_to_sentence('roh roh raggy')
    assert sentence == 'Roh roh raggy.'


# 4. Fixed the failing is_long_word function
# (don't change the tests, change the function!)

def phrase_to_sentence(phrase):
    """format a phrase as a sentence
    starting with a capital and ending with a single full stop.
    Important: start with a function header and just use pass as the body
    t   hen add doctests for 3 tests:
    'hello' -> 'Hello.'
    'It is an ex parrot.' -> 'It is an ex parrot.'
    and one more you decide (one that is valid!)
    test this and watch the tests fail
    then write the body of the function so that the tests pass"""
    sentence = phrase.capitalize()
    if sentence[-1] != '.':
        sentence += '.'
    return sentence


run_tests()

# 3. Uncommented the following line and run the doctests
# (PyCharm may see your >>> doctest comments and run doctests anyway.)

doctest.testmod()
