#!/usr/bin/env python3
"""
Create a Cache class. In the __init__ method, store an instance of the Redis
"""
import redis
import sys
import uuid


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
