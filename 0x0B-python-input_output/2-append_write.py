#!/usr/bin/python3
"""Defines The append text function"""


def append_write(filename="", text=""):
    """appends a string and returns the number of characters added

    Args:
        filename: file name param
        text (str): text to append

    Return: the number of character added
    """
    with open(filename, "a", encoding="utf-8") as file:
        lines = file.write(text)
        return lines
