#!/usr/bin/env python3
"""
This module is to define Simple pagination using index_range
"""
from typing import List
import csv
from typing import Tuple


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    Returns a tuple of start index and end index for pagination.
    """
    start_in = (page - 1) * page_size
    end_in = start_in + page_size
    return start_in, end_in


class Server:
    """
    define server class to paginate a database of popular baby names
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        self.__dataset = None

    def dataset(self) -> List[List]:
        """
        define Cached dataset
        """
        if self.__dataset is None:
            with open(self.DATA_FILE) as f:
                reader = csv.reader(f)
                dataset = [row for row in reader]
            self.__dataset = dataset[1:]

        return self.__dataset

    def get_page(self, page: int = 1, page_size: int = 10) -> List[List]:
        """
        Returns the specified page of the dataset
        """
        assert isinstance(page, int) and page > 0,
        "Page must be a positive integer"
        assert isinstance(page_size, int) and page_size > 0,
        "Page size must be a positive integer"

        start, end = index_range(page, page_size)
        return self.dataset()[start:end]
