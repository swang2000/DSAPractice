def combine(n, k):
    if k == 0:
        return [[]]
    return [pre + [i] for i in range(k, n + 1) for pre in combine(i - 1, k - 1)]


combine(4, 2)