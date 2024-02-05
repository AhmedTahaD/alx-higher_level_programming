#!/usr/bin/python3
"""Defines Module for lookup method"""


def lookup(obj):
    """Return a list of an object's available attributes.

    param:
        obj: the object to list

    Return:
        returns the list of available attributes"""
    return (dir(obj))
