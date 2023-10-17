#!/usr/bin/env python3
""" redis client """


import redis
from typing import Union, callable, Optional
import uuid


class Cache():
    """ redis cache """

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """ store to redis """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Optional[Callable] = None) -> Union[
        str,
        bytes,
        int,
        float
    ]:
        """ get from redis """
        data = self._redis.get(key)
        if fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """ get string from redis """
        return self.get(key, str)

    def get_int(self, key: str) -> int:
        """ get int from redis """
        return self.get(key, int)
