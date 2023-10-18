#!/usr/bin/env python3
""" redis client """


import redis
from typing import Union, Callable, Optional
import uuid
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """ count calls decorator """
    key = method.__qualname__

    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper function """
        self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """ call history decorator """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """ Wrapper function """
        input = str(args)
        self._redis.rpush(method.__qualname__ + ":inputs", input)
        output = str(method(self, *args, **kwargs))
        self._redis.rpush(method.__qualname__ + ":outputs", output)
        return output

    return wrapper


def replay(method: Callable):
    """ replay decorator """
    r = redis.Redis()
    funk = method.__qualname__
    count = r.get(funk).decode("utf-8")
    inputs = r.lrange(funk + ":inputs", 0, -1)
    outputs = r.lrange(funk + ":outputs", 0, -1)
    print(f"{funk} was called {count} times:")
    for i, o in zip(inputs, outputs):
        print(f"{funk}(*{i.decode('utf-8')}) -> {o.decode('utf-8')}")


class Cache():
    """ redis cache """

    def __init__(self) -> None:
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
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
