#!/usr/bin/python3
"""
This module is to define MRUCache
"""
from base_caching import BaseCaching


class MRUCache(BaseCaching):
    """
    MRUCache inherits from BaseCaching and
    is a caching system with MRU policy.
    """

    def __init__(self):
        """
        Initialize the MRUCache
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add an item in the cache using MRU policy
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                discarded_key = self.order.pop()
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key using MRU policy
        """
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
        return self.cache_data.get(key) if key is not None else None
