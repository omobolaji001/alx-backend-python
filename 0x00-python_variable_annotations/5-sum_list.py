#!/usr/bin/env python3
""" A script for type-annoted function that takes
list of floats as an argument and returns their sum
as a float.
"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """ Calculates the sum of the argument

    Args:
            input_list (list): list of floating numbers

    Returns:
            float: sum of the floats in the list
    """

    return float(sum(input_list))
