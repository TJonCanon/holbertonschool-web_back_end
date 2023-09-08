#!/usr/bin/env python3
"""  asynchronous coroutine that takes
    an integer, waits, then returns it """


import asyncio
from random import uniform


async def wait_random(max_delay: int = 10) -> float:
    """ returns random number"""
    delay = uniform(0, max_delay)
    await asyncio.sleep(delay)
    return delay
