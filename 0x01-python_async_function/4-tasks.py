#!/usr/bin/env python3
"""More asyncio create task"""
import asyncio
from typing import List


task_wait_random = __import__('3-tasks').task_wait_random


async def task_wait_n(n: int, max_delay: int) -> List[float]:
    """Calls task_wait_random from previous task"""

    res = await asyncio.gather(
        *(task_wait_random(max_delay) for i in range(n))
        )
    return sorted(res)
