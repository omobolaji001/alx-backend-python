#!/usr/bin/env python3
"""A script for typed-annoted function that takes two
strings as arguments and returns a concatenated string.
"""


def concat(str1: str, str2: str) -> str:
    """ Concatenates the two arguments

    Args:
            str1 (str): first argument
            str2 (str): second argument

    Returns:
            str: concatenated string
    """
    return "{}{}".format(str1, str2)
