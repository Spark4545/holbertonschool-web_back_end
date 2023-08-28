#!/usr/bin/env python3
"""
    Module with typing Python
"""

from typing import Iterable, Sequence, List, Tuple


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """element_length

    Args:
        lst (Iterable[Sequence]): all element of the list

    Returns:
        List ([Tuple, int]) : list of tuple and int
    """
    return [(i, len(i)) for i in lst]
