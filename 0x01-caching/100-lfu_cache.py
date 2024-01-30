#!/usr/bin/python3
"""
This module is to define LFUCache
"""
from base_caching import BaseCaching


class LFUCache(BaseCaching):
    """
    LFUCache inherits from BaseCaching and
    is a caching system with LFU policy.
    """

    def __init__(self):
        """
        Initialize the LFUCache.
        """
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """
        Add an item to the cache
        """
        if key is not None and item is not None:
            if len(self.cache_data) >= self.MAX_ITEMS:
                m_frq = min(self.frequency.values())
                lf_key = [k for k, v in self.frequency.items() if v == m_frq]

                if len(lf_key) > 1:
                    lru_key = min(lf_key, key=lambda k: self.frequency[k])
                    lf_key = [lru_key]

                discarded_key = lf_key[0]
                print("DISCARD:", discarded_key)
                del self.cache_data[discarded_key]
                del self.frequency[discarded_key]

            self.cache_data[key] = item
            self.frequency[key] = self.frequency.get(key, 0) + 1

    def get(self, key):
        """
        Get an item from the cache by key
        """
        if key in self.cache_data:
            self.frequency[key] = self.frequency.get(key, 0) + 1
            return self.cache_data[key]
        else:
            return None
