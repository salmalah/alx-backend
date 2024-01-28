#!/usr/bin/env python3
"""
This module is to define Hypermedia pagination sample
"""
from typing import Dict, List, Tuple
import csv
import math


def index_range(page: int, page_size: int) -> Tuple[int, int]:
    """
    define retrieves the index range from a given page and page size
    """
    start_in = (page - 1) * page_size
    end_in = start_in + page_size
    return (start_in, end_in)


class Server:
    """
    define Server class to paginate a database of popular baby names
    """
    DATA_FILE = "Popular_Baby_Names.csv"

    def __init__(self):
        """
        Initializes a new instance
        """
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
        define retrieves a page of data
        """
        assert type(page) == int and type(page_size) == int
        assert page > 0 and page_size > 0
        start, end = index_range(page, page_size)
        data = self.dataset()
        if start > len(data):
            return []
        return data[start:end]

    def get_hyper(self, page: int = 1, page_size: int = 10) -> Dict:
        """
        retrieves information about a page.
        """
        page_data = self.get_page(page, page_size)
        start, end = index_range(page, page_size)
        total_pages = math.ceil(len(self.__dataset) / page_size)
        page_info = {
            'page_size': len(page_data),
            'page': page,
            'data': page_data,
            'next_page': page + 1 if end < len(self.__dataset) else None,
            'prev_page': page - 1 if start > 0 else None,
            'total_pages': total_pages,
        }
        return page_info
