#!/usr/bin/python3
"""Module for add_integer method."""


def add_integer(a, b=98):
    """ function that adds 2 integers.
    Args:
        a: first number.
        b: second number, default 98.

    Raises:
        TypeError: if a and b are not integer, float.

    Returns:
        the summation of two integers.
    """

    if type(a) not in (float, int):
        raise TypeError("a must be an integer")
    if type(b) not in (float, int):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
