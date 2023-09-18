#!/usr/bin/env python3
"""
    class that inherits from BaseCaching and is a caching system
"""
BaseCaching = __import__("base_caching").BaseCaching


class BasicCache(BaseCaching):
    """ no-limit caching system """

    def put(self, key, item):
        """ assigns to cache_data in the form of key:item  """
        if key and item:
            self.cache_data[key] = item

    def get(self, key):
        """ return value in cache_data linked to key """
        return self.cache_data[key] if key in self.cache_data else None
    