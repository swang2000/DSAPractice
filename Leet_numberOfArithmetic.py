def numberOfArithmeticSlices(A):
    out = [0]*(len(A))
    k = 1
    for i in range(2,len(A)):
        if A[i] - A[i-1] == A[i-1] - A[i-2]:
            out[i] = (out[i-1]+k)
            k += 1
        else:
            out[i] =out[i-1]
            k =1
    return out[-1]

A = [1, 3, 5, 7, 9]
numberOfArithmeticSlices(A)



