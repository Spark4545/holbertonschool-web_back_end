#!/usr/bin/env python3
"""
    Module with typing Python
"""

from typing import List, Union


def sum_mixed_list(mxd_list: List(Union[int, float])) -> float:
    """
    Args:
        mxd_list: list of ints and floats

        Returns:
            sum of items in mxd_list
    """
    total = 0.0

    for item in mxd_list:
        total += item

    return total
