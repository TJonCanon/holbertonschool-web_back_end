#!/usr/bin/env python3
"""   FIFO caching system inheriting from BaseCaching """
BaseCaching = __import__("base_caching").BaseCaching


class FIFOCache(BaseCaching):
    """ first-in-first-out caching system inheriting from BaseCaching """

    def __init__(self):
        """ new init func with cache list """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """ assigns key: item to self.cache_data if they both exist
            as long as the cache has not exceeded MAX_ITEMS """
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                popper = self.queue.pop(0)
                print(f"DISCARD: {popper}")
                del self.cache_data[popper]
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ return value in cache_data linked to key """
        return self.cache_data[key] if key in self.cache_data else None
