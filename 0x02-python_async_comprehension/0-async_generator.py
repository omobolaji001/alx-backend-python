#!/usr/bin/env python3
"""A script that defines asynchronous generator to
to yield random numbers.
"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Generates 10 random numbers between 0, 10
    """
    for num in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
