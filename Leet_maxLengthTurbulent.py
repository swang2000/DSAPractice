def maxTurbulenceSize(A):
    lens, best = 0, 0
    for i in range(len(A)):
        if i >= 2 and (A[i - 2] > A[i - 1] < A[i] or A[i - 2] < A[i - 1] > A[i]):
            lens += 1
        elif i >= 1 and A[i] != A[i - 1]:
            lens = 2
        else:
            lens = 1
        best = max(best, lens)
    return best

A = [9,4,2,10,7,8,8,1,9]
maxTurbulenceSize(A)