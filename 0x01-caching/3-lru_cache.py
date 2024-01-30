#!/usr/bin/python3
"""
This module is to define LRUCache
"""
from base_caching import BaseCaching


class LRUCache(BaseCaching):
    """
    This LRUCache inherits from BaseCaching and
    is a caching system with LRU policy.
    """

    def __init__(self):
        """
        Initialize the LRUCache
        """
        super().__init__()
        self.order = []

    def put(self, key, item):
        """
        Add item in the cache using LRU policy
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.order.remove(key)
            elif len(self.cache_data) >= self.MAX_ITEMS:
                discarded_key = self.order.pop(0)
                del self.cache_data[discarded_key]
                print("DISCARD: {}".format(discarded_key))
            self.order.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """
        Get an item by key using LRU policy
        """
        if key in self.cache_data:
            self.order.remove(key)
            self.order.append(key)
        return self.cache_data.get(key) if key is not None else None
