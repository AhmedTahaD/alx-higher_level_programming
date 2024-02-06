#!/usr/bin/python3
"""Defines The read_file function"""


def read_file(filename=""):
    """""reads a text file(UTF8) and prints it to stdout
    Args:
        filename: the file to read
    """
    with open(filename, "r", encoding="utf-8") as file:
        files = file.read()
        print(files, end="")
