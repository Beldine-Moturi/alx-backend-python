#!/usr/bin/env python3
"""Defines a function sum_list"""


def sum_list(input_list: list[float]) -> float:
    """Returns the sum of input_list floats"""

    sum = 0.0
    for num in input_list:
        sum += num
    return sum
