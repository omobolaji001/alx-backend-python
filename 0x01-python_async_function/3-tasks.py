#!/usr/bin/env python3
""" A script that defines a function to handle asyncio task
"""
import asyncio
from asyncio import Task
from typing import Any
wait_random = __import__("0-basic_async_syntax").wait_random


def task_wait_random(max_delay: int) -> Task[Any]:
    """ Returns asyncio.Task
    """
    task = asyncio.create_task(wait_random(max_delay))

    return task
