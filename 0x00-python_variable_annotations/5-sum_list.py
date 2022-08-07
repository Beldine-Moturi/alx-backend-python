#!/usr/bin/env python3
"""Defines a function sum_list"""
from typing import List


def sum_list(input_list: List[float]) -> float:
    """Returns the sum of input_list floats"""

    sum = 0.0
    for num in input_list:
        sum += num
    return sum
