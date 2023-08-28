#!/usr/bin/env python3
""" Async Generator """

import time
import asyncio


async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_time() -> float:
    """
    Args:
        Void

    Returns:
        float random
    """
    first_time = time.perf_counter()
    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)
    elapsed = time.perf_counter()

    return (elapsed - first_time)
