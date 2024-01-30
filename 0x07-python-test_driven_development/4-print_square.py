#!/usr/bin/python3
"""Function for print a square"""


def print_square(size):
    """function that prints a square with the character #.

    Args:
    size: is the size length of the square

    Raises:
    typeError: if size is not ineger.or if size is float.
    valueError: if size is < 0.
    """

    if type(size) is not int:
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    print((("#" * size + "\n") * size), end="")


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/4-print_square.txt")
