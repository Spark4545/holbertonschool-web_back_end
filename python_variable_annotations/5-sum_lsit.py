#!/usr/bin/env python3
"""
    Module with typing Python
"""

from typing import List


def sum_list(input_list: List[float]) -> float:
    """
    Args:
        input_list: list of float

    Returns:
        sum of all floats in input_list
    """
    total = 0.0

    for item in input_list:
        total += item

    return total
