#!/usr/bin/python3
"""Function to add two integer"""


def add_integer(a, b=98):
    """Add_integer

    
    a: firstintegers
    b:second integer
    
    raise a TypeError exception
    if a, b are not int or float
    
    Returns an integer: the addition of two integers.
    """
    
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")
    return int(a) + int(b)


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/0-add_integer.txt")
