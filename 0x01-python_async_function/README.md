# 0x01. Python - Async

This project focuses on asynchronous programming in Python. It covers various concepts and techniques related to async/await, asyncio, and concurrent coroutines, providing a hands-on approach to understanding asynchronous programming in Python.


## Learning Objectives

- Understand and use `async` and `await` syntax.
- Execute asynchronous programs with asyncio.
- Run concurrent coroutines.
- Create asyncio tasks.
- Utilize the random module in Python.

## Requirements

- All files should be written in Python 3 (version 3.7), tested on Ubuntu 18.04 LTS.
- Every file should start with `#!/usr/bin/env python3`.
- Code should follow the pycodestyle (version 2.5.x).
- Functions and coroutines must be type-annotated.
- All modules and functions should have documentation.

## Resources

- [Async IO in Python: A Complete Walkthrough](link)
- [Asyncio - Asynchronous I/O](link)
- [Random.uniform](link)

## Tasks

### 0. The Basics of Async

Develop an asynchronous coroutine that takes an integer argument `max_delay` (default=10) and returns a random delay.

- **File:** `0-basic_async_syntax.py`

### 1. Execute Multiple Coroutines

Implement `wait_n` that takes two int arguments `n` and `max_delay`, spawning `wait_random` n times.

- **File:** `1-concurrent_coroutines.py`

### 2. Measure the Runtime

Create a function `measure_time` that measures the total execution time for `wait_n(n, max_delay)`.

- **File:** `2-measure_runtime.py`

### 3. Tasks

Develop a function `task_wait_random` that takes an integer `max_delay` and returns an asyncio.Task.
