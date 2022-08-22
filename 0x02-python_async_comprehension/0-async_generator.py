#!/usr/bin/env python3
"""Defines a coroutine"""
import asyncio
import random
from typing import Generator


async def async_generator() -> Generator[float, None, None]:
    """Yields random numbers between 1 and 10"""

    for i in range(10):
        await asyncio.sleep(1)
        yield random.uniform(0, 10)
