#!/usr/bin/env python3
"""   collect 10 random numbers using an async comprehension
    over async_generator, then return the 10 random numbers """


from typing import List
import asyncio
async_generator = __import__("0-async_generator").async_generator


async def async_comprehension() -> List[float]:
    """ collects and returns 10 numbers asynchronously """
    return [i async for i in async_generator()]
