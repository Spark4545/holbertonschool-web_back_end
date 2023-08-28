#!/usr/bin/env python3
""" Basic syntax await async """

import asyncio
import time
from typing import List


wait_n = __import__('1-concurrent_coroutines').wait_n


def measure_time(max_delay: int = 10, n: int = 0) -> float:
    """
    Args:
        max_delay (int): max delay
        n (int): number of time

    Returns:
        total_time (float): float
    """
    first_time = time.perf_counter()
    asyncio.run(wait_n(max_delay, n))
    elapsed = time.perf_counter() - first_time
    total_time = elapsed / n

    return total_time
