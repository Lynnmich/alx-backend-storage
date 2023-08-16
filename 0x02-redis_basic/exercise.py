#!/usr/bin/env python3
"""
Create a Cache class. In the __init__ method, store an instance of the Redis
"""
import redis
import sys
import uuid
from typing import Any, Callable, Union



def count_calls(method: Callable) -> Callable:
    """Keeps track of the number of calls made to a method in a Cache class"""
    @wraps(method)
    def callcounter(self, *args, **kwargs) -> Any:
        """Invokes the given method after incrementing its call counter"""
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return callcounter

def call_history(method: Callable) -> Callable:
    """Keeps track of the call details of a method in a Cache class"""
    @wraps(method)
    def callcounter(self, *args, **kwargs) -> Any:
        """Returns the output after storing its input and output keys"""
        in_key = '{}:inputs'.format(method.__qualname__)
        out_key = '{}:outputs'.format(method.__qualname__)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(in_key, str(args))
        output = method(self, *args, **kwargs)
        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(out_key, output)
        return output
    return callcounter


class Cache:
    """Create Cache class"""
    def __init__(self) -> None:
        """ Instance of Cache class """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """the method takes a data argument and returns a string"""
        key = uuid.uuid4()
        self._redis.set(str(key), data)
        return str(key)

    def get(self, key: str, fn: Optional[Callable] = None) ->\
            Union[str, bytes, int, float]:
        """retieves value from server, converts it to the desired format"""
        return fn(self._redis.get(key)) if fn else self._redis.get(key)

    def get_int(self, data_bytes: bytes) -> int:
        """converts data bytes from server to int"""
        return int.from_bytes(data_bytes, sys.byteorder)

    def get_str(self, data_bytes: bytes) -> str:
        """converts data bytes from server to str"""
        return data_bytes.decode('utf-8')
