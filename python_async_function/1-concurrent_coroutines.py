#!/usr/bin/env python3
"""
    Import wait_random from the previous python file that you've written
    and write an async routine called wait_n that takes in 2 int
    arguments (in this order): n and max_delay. You will
    spawn wait_random n times with the specified max_delay.
"""


from typing import List
import asyncio
wait_random = __import__("0-basic_async_syntax").wait_random


async def wait_n(n: int, max_delay: int) -> List[float]:
    """ wait_n should return the list of all the delays
        (float values). The list of the delays should be in
        ascending order without using sort() because of concurrency. """
    # make a list of the tasks
    tasks = asyncio.as_completed([
        asyncio.create_task(
            wait_random(max_delay)
        ) for _ in range(n)
    ])
    # create a list of delay times
    wait_list = []
    # loop thru the tasks and append to wait times
    for task in tasks:
        result = await task
        wait_list.append(result)
    # return wait times
    return wait_list
