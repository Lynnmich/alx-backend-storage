#!/usr/bin/env python3
"""
Create a Cache class. In the __init__ method, store an instance of the Redis
"""
import redis


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
