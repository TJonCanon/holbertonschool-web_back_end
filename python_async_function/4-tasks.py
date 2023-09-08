#!/usr/bin/env python3
""" Use wait_n and change it into a
    new function task_wait_n. The code is almost the same
    to wait_n except task_wait_random is being called. """


from typing import List
import asyncio
task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """task_wait_n function declaration"""
    delays = []
    tasks = []
    for i in range(n):
        task = task_wait_random(max_delay)
        tasks.append(task)

    for task in tasks:
        delay = await task
        delays.append(delay)

    return sorted(delays)
