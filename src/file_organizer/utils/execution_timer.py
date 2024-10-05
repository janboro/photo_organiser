from collections.abc import Callable
from time import perf_counter
from typing import Any


def timeit(func_mode: str) -> Any:
    def decorator(function: Callable[[Any], Any]) -> Any:
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            start = perf_counter()
            result = function(*args, **kwargs)
            stop = perf_counter()
            print(f"Took {stop - start} to {func_mode}")
            return result

        return wrapper

    return decorator
