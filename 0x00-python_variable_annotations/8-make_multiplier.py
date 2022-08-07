#!/usr/bin/env python3
"""Defines a function make_multiplier"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by multiplier"""

    def func(num):
        return num * multiplier
    return func
