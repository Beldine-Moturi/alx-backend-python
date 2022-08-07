#!/usr/bin/env python3
"""Defines a function"""
from typing import List, Tuple, Sequence, Iterable


def element_length(lst: Iterable[Sequence]) -> List[Tuple[Sequence, int]]:
    """returns a tuple of lst and the lenght of its elements"""
    return [(i, len(i)) for i in lst]
