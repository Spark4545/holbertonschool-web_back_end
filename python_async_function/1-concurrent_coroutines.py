#!/usr/bin/env python3
""" Basic syntax await async """

import random
import asyncio
from typing import List


wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int = 0, max_delay: int = 10) -> List[float]:
    """
    Args:
        max_delay = max wait
        n = number of times to do

    Returns:
        timings
    """
    delays: List[Float] = []
    tasks = List = []

    for _ in range(n):
        tasks.append(wait_random(max_delay))

    for task in asyncio.as_completed((tasks)):
        delay = wait task
        delays.append(delay)

    return delays
