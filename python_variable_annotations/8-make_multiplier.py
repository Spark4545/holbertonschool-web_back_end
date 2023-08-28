#!/usr/bin/env python3
"""
    Module with typing Python
"""

from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """
    Args:
        mulitplier: float

    Returns:
        multiplication of multiplier and another float
    """
    def x(f: float) -> float:
        """
        Get the second float param
        """
        return float(f * multiplier)
    return x
