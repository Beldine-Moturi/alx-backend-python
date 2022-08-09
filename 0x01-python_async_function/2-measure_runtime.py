#!/usr/bin/env python3
"""Defines an async coroutine"""
import time
import asyncio


wait_n = __import__('1-concurrent_coroutines').wait_n


async def measure_time(n: int, max_delays: int) -> float:
    """calcultes execution time for a coroutine"""

    start = time.perf_counter()
    await wait_n(n, max_delays)
    total_time = time.perf_counter() - start
    return total_time / n
