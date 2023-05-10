#!/usr/bin/env python3
""" module exercise.py for using the Redis NoSQL data storage """

import redis
import uuid
from typing import Union


class Cache:
    """
    A class for caching data in Redis.
    Attributes:
        _redis (redis.Redis): A Redis client instance.
    Methods:
        store(data: Union[str, bytes, int, float]) -> str:
            Stores data in Redis and returns the key for retrieval.
    """
    def __init__(self):
        """Initializes a new Redis client and flushes its database."""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Stores data in Redis and returns the key for retrieval.
        Args:
            data (Union[str, bytes, int, float]): data to be stored in Redis
        Returns:
            str: The key used to store the data in Redis.
        """
        key = str(uuid.uuid4())
        self._redis.set(key, data)
        return key
