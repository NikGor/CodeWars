def series_sum(n):
    if n == 0:
        return '0,00'
    else:
        return '{:.2f}'.format(sum([1 / (1 + 3 * i) for i in range(n)]))
