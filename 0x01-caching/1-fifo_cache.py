#!/usr/bin/python3
"""
This module is to define FIFOCache
"""
from base_caching import BaseCaching


class FIFOCache(BaseCaching):
    """
    FIFOCache inherits from BaseCaching and
    is a caching system with FIFO policy
    """

    def __init__(self):
        """
        Initialize FIFOCache
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item in the cache using FIFO policy
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                discarded_key = self.order.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key using FIFO policy
        """
        return self.cache_data.get(key) if key is not None else None
