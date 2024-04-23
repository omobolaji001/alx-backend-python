#!/usr/bin/env python3
""" A script that defines a function to calculate
the runtime of concurrent coroutines.
"""
import asyncio
import time
wait_n = __import__("1-concurrent_coroutines").wait_n


def measure_time(n: int, max_delay: int) -> float:
    """Returns average runtime of the execution
    concurrent coroutines
    """
    start = time.perf_counter()
    asyncio.run(wait_n(n, max_delay))
    elapsed_time = time.perf_counter() - start

    return elapsed_time / n
