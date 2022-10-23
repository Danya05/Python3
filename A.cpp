def pascal_triangle():
    cache_prev = []
    cnt_len_row = 1
    while True:
        cache_curr = []
        for i in range(cnt_len_row):
            if i == 0 or i == cnt_len_row - 1:
                cache_curr.append(1)
            else:
                cache_curr.append(cache_prev[i - 1] + cache_prev[i])
        cache_prev = cache_curr[:]
        cnt_len_row += 1
        yield from cache_curr
