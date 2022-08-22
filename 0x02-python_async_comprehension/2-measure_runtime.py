#!/usr/bin/env python3
"""Defines a coroutine"""
import asyncio
import time

async_comprehension = __import__('1-async_comprehension').async_comprehension


async def measure_runtime() -> float:
    """Measures runtime of parallel async coroutines"""

    start = time.perf_counter()
    result = await asyncio.gather(*(async_comprehension() for i in range(4)))
    total_time = time.perf_counter() - start
    return total_time
