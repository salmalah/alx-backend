#!/usr/bin/python3
"""
This module is to define LIFOCache
"""
from base_caching import BaseCaching


class LIFOCache(BaseCaching):
    """
    LIFOCache inherits from BaseCaching and
    is a caching system with LIFO policy.
    """

    def __init__(self):
        """
        Initialize the LIFOCache module
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item in the cache using LIFO policy
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                discarded_key = self.order.pop()
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key using LIFO policy
        """
        return self.cache_data.get(key) if key is not None else None
