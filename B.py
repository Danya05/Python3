from heapq import merge


def merge_sorter(*args):
    yield from merge(*args)
