#!/usr/bin/env python3
""" A script that defines a coroutine to calculate the runtime
for four parallel comprehensions using asyncio.gather()
"""
import asyncio
import time
async_comprehension = __import__("1-async_comprehension").async_comprehension


async def measure_runtime() -> float:
    """ Returns the runtime of 
    four parallel comprehensions
    """
    start = time.perf_counter()

    tasks = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*tasks)

    return time.perf_counter() - start
