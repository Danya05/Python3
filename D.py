import functools
from collections import OrderedDict


def cache(N):
    dct = OrderedDict()

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            tpl = tuple(args) + tuple(kwargs.values())
            h = hash(tpl)
            if h not in dct:
                dct[h] = func(*args, **kwargs)
            if len(dct) > N:
                dct.popitem(False)
            return dct[h]
        return wrapper
    return decorator

