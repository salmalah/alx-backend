#!/usr/bin/env python3
"""
This module is the define a function named index_range that takes two integer arguments page and page_size
"""
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple of start index and end index for pagination
    """
    start_in = (page - 1) * page_size
    end_in = start_in + page_size
    return (start_in, end_in)
