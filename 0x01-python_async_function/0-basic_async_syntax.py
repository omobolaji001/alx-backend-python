#!/usr/bin/env python3
""" A script that defines asynchronous function
"""
import asyncio
import random


async def wait_random(max_delay: int = 10) -> float:
    """Returns a random number between 0 and max_delay.
    """
    sec = random.uniform(0, max_delay)
    await asyncio.sleep(sec)

    return sec
