import functools
from time import perf_counter


def profiler(func):
    a = 0
    b = 0

    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        nonlocal a, b
        b += 1
        a += 1
        start = perf_counter()
        var = func(*args, **kwargs)
        b -= 1
        end = perf_counter()
        wrapper.last_time_taken = end - start
        wrapper.calls = a
        if b == 0:
            a = 0
        return var
    return wrapper

