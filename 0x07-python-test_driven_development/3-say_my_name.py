#!/usr/bin/python3
"""Module to print name"""


def say_my_name(first_name, last_name=""):
    """Function to print my name is <first name> <last name>

    Args:
    first_name: name first string
    last_name: name last string

    Raises:
    TypeError: If first_name or last_name are not strings.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {:s} {:s}".format(first_name, last_name))


if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/3-say_my_name.txt")
