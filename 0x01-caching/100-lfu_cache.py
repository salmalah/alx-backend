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
        Initialize the LFUCache
        """
        super().__init__()
        self.frequency = {}

    def put(self, key, item):
        """
        Add item in the cache using LFU policy
        """
        if key is not None and item is not None:
            if key in self.cache_data:
                self.frequency[key] += 1
            elif len(self.cache_data) >= self.MAX_ITEMS:
                # Find the least frequency used items
                min_frequency = min(self.frequency.values())
                least_frequent_keys = [k for k, v in self.frequency.items() if v == min_frequency]
                # If more than one item with the least frequency, use LRU to discard
                if len(least_frequent_keys) > 1:
                    lru_key = min(self.order, key=self.order.get)
                    least_frequent_keys.remove(lru_key)
                    discarded_key = min(least_frequent_keys, key=self.order.get)
                else:
                    discarded_key = least_frequent_keys[0]
                del self.cache_data[discarded_key]
                del self.frequency[discarded_key]
                print("DISCARD: {}".format(discarded_key))
                self.order.pop(self.order.index(discarded_key))

            self.cache_data[key] = item
            self.frequency[key] = 1
            self.order.append(key)

    def get(self, key):
        """
        Get an item by key using LFU policy
        """
        if key in self.cache_data:
            self.frequency[key] += 1
            return self.cache_data[key]
        return None
