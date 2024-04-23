#!/usr/bin/env python3
"""A script that defines asynchronous function
to execute multiple coroutines ata the same time with async
"""
import asyncio
from typing import List
wait_random = __import__('0-basic_async_syntax').wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """Returns the list of all delays (float values)
    """
    tasks = [wait_random(max_delay) for i in range(n)]

    return sorted(await asyncio.gather(*tasks))
