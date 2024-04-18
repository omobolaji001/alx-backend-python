#!/usr/bin/env python3
""" A script for type-annoted function that takes
a float as argument and returns the floor of the float.
"""
import math


def floor(n: float) -> int:
    """Takes a float argument and returns its floor value

    Args:
            n (float): the float argument

    Returns:
            int: the floored value of the argument
    """
    return math.floor(n)
