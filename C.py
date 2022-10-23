import sys
import functools


def takes(*args1):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args2):
            j = 0
            for i in args1:
                if j == len(args2):
                    break
                if not isinstance(args2[j], i):
                    raise TypeError
                j += 1
            return func(*args2)
        return wrapper
    return decorator


exec(sys.stdin.read())
