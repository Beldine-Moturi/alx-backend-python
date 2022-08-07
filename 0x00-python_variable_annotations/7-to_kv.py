#!/usr/bin/env python3
"""Defines a function to_kv"""
from typing import Union, Tuple


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """Returns a tuple of its arguments"""

    return (k, float(v ** 2))
