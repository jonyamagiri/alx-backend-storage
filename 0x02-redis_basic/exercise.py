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
        get(key: str, fn: Optional[Callable[[bytes], Any]] = None) -> Any:
            Retrieves data from Redis using the specified key and converts it
            to the desired format using the provided conversion function (if
            any).
        get_str(key: str) -> str:
            Retrieves a string value from Redis using the specified key.
        get_int(key: str) -> int:
            Retrieves an integer value from Redis using the specified key.
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


    def get(self, key: str, fn: Optional[Callable[[bytes], Any]] = None) -> Any:
        """
        Retrieves data from Redis using the specified key and converts it
        to the desired format using the provided conversion function (if any).
        Args:
            key (str): The key used to store the data in Redis.
            fn (Optional[Callable[[bytes], Any]]): The conversion function to
                use to convert the retrieved data to the desired format.
        Returns:
            Any: The retrieved data in the desired format.
        """
        value = self._redis.get(key)
        if value is None:
            return value
        if fn is not None:
            value = fn(value)
        return value

    def get_str(self, key: str) -> str:
        """
        Retrieves a string value from Redis using the specified key.
        Args:
            key (str): The key used to store the string value in Redis.
        Returns:
            str: The retrieved string value.
        """
        return self.get(key, fn=lambda x: x.decode())

    def get_int(self, key: str) -> int:
        """
        Retrieves an integer value from Redis using the specified key.
        Args:
            key (str): The key used to store the integer value in Redis.
        Returns:
            int: The retrieved integer value.
        """
        return self.get(key, fn=int)
