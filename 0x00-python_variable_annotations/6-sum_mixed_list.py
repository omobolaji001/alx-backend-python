#!/usr/bin/env python3
"""A script for type-annotated function that takes
a list of integers and floats and returns their sum
as a float.
"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """ Calculates the sum of the argument

    Args:
            input_list (list): list of floating numbers

    Returns:
            float: sum of the floats in the list
    """
    return float(sum(mxd_lst))
