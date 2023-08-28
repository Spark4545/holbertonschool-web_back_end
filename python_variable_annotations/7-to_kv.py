#!/usr/bin/env python3
"""
    Module with typing Python
"""

from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """
    Args:
        k: string
        v: int or float

    Returns:
        Tuple of k, v where k: str and squared v: float
    """
    return k, float(v ** 2)
