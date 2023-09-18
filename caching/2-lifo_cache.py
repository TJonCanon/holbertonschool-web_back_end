#!/usr/bin/env python3
""" LIFO caching system inheriting from BaseCaching """
BaseCaching = __import__("base_caching").BaseCaching


class LIFOCache(BaseCaching):
    """ last-in-first-out cache system """

    def __init__(self):
        """ new init func """
        super().__init__()
        self.queue = []

    def put(self, key, item):
        """assigns key: item to self.cache_data if they both exist
            as long as the cache has not exceeded MAX_ITEMS

            pops it off if it has """
        if key and item:
            if len(self.cache_data) >= self.MAX_ITEMS:
                popper = self.queue.pop()
                print(f"DISCARD: {popper}")
                del self.cache_data[popper]
            self.queue.append(key)
            self.cache_data[key] = item

    def get(self, key):
        """ return value in cache_data linked to key """
        return self.cache_data[key] if key in self.cache_data else None
    