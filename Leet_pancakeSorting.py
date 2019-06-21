def pancakeSort(A):
    n = len(A)
    key = n
    out = []
    while key > 0:
        j = A.index(key)
        if j != 0:
            A[:j + 1] = A[:j + 1][::-1]
        A[:key] = A[:key][::-1]
        out.extend([j + 1, key])
        key -= 1
    return out

A = [4,2,3,1]
pancakeSort(A)
