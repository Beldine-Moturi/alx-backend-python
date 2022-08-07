#!/usr/bin/env python3
"""Defines a function sum_mixed_list"""
from typing import List, Union


def sum_mixed_list(mxd_lst: List[Union[int, float]]) -> float:
    """Returns sum of mxd_lst as a float"""

    return sum(mxd_lst)
