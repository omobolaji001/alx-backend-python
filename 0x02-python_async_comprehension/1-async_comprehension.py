#!/usr/bin/env python3
"""A script that defines a coroutine to return random numbers
"""
import asyncio
from typing import List
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """ Returns list of random numbers
    """
    return [i async for i in async_generator()]
