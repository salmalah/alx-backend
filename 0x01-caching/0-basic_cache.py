#!/usr/bin/python3
"""
This module is to define BasicCache module
"""
from base_caching import BaseCaching


class BasicCache(BaseCaching):
    """
    BasicCache inherits from BaseCaching and
    is a caching system without a limit.
    """

    def put(self, key, item):
        """
        Add an item in the cache without any limit
        """
        if key is not None and item is not None:
            self.cache_data[key] = item

    def get(self, key):
        """
        Get item by key
        """
        return self.cache_data.get(key) if key is not None else None
