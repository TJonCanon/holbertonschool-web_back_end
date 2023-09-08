#!/usr/bin/env python3
"""   execute async_comprehension
    four times in parallel using asyncio.gather

    measure_runtime should measure the total runtime and return it """


import asyncio
async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """measure_runtime function declaration"""
    start = asyncio.get_running_loop().time()
    coroutines = [async_comprehension() for _ in range(4)]
    await asyncio.gather(*coroutines)
    end = asyncio.get_running_loop().time()
    return end - start
