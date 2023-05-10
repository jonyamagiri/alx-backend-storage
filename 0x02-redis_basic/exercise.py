#!/usr/bin/env python3
""" module exercise.py for using the Redis NoSQL data storage """

import uuid
import redis
from functools import wraps
from typing import Any, Callable, Union


def count_calls(method: Callable) -> Callable:
    """Tracks the number of calls made to a method in a Cache class."""
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """Invokes the given method after incrementing its call counter."""
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)

        return method(self, *args, **kwargs)

    return wrapper


def call_history(method: Callable) -> Callable:
    """Tracks the call details of a method in a Cache class."""
    @wraps(method)
    def wrapper(self, *args, **kwargs) -> Any:
        """Returns the method's output after storing its inputs and output."""
        in_key = f"{method.__qualname__}:inputs"
        out_key = f"{method.__qualname__}:outputs"

        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(in_key, str(args))

        output = method(self, *args, **kwargs)

        if isinstance(self._redis, redis.Redis):
            self._redis.rpush(out_key, output)

        return output

    return wrapper


def replay(fn: Callable) -> None:
    """ Displays the call history of a Cache class' method. """
    redis_store = getattr(fn.__self__, '_redis', None)
    if not isinstance(redis_store, redis.Redis):
        return

    fxn_name = fn.__qualname__
    in_key = f"{fxn_name}:inputs"
    out_key = f"{fxn_name}:outputs"
    fxn_call_count = redis_store.get(fxn_name) or 0

    print(f"{fxn_name} was called {fxn_call_count} times:")

    fxn_inputs = redis_store.lrange(in_key, 0, -1)
    fxn_outputs = redis_store.lrange(out_key, 0, -1)

    for fxn_input, fxn_output in zip(fxn_inputs, fxn_outputs):
        print(f"{fxn_name}(*{fxn_input.decode()}) -> {fxn_output.decode()}")


class Cache:
    """Represents an object for storing data in a Redis data storage."""
    def __init__(self) -> None:
        """Initializes a Cache instance."""
        self._redis = redis.Redis()
        self._redis.flushdb(True)

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """Stores a value in a Redis data storage and returns the key."""
        data_key = str(uuid.uuid4())
        self._redis.set(data_key, data)
        return data_key


    def get(self,
            key: str,
            fn: Callable = None) -> Union[str,
                                          bytes,
                                          int,
                                          float]:
        """Retrieves a value from a Redis data storage."""
        data = self._redis.get(key)

        if fn is not None:
            data = fn(data)

        return data


    def get_str(self, key: str) -> str:
        """Retrieves a string value from a Redis data storage."""
        data = self.get(key, lambda x: x.decode('utf-8'))
        return data


    def get_int(self, key: str) -> int:
        """Retrieves an integer value from a Redis data storage."""
        data = self.get(key, int)
        return data
