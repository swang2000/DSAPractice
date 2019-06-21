
def lenLongestFibSubseq(A):
    n = len(A)
    dp = [[2]*n for _ in range(n)]
    for i in range(1, n):
        for j in range(i+1, n):
            temp = A[j] - A[i]
            if temp in A[:i]:
                k = A.index(temp)
                if 0 <= k < i:
                    dp[i][j] = dp[k][i] +1
    return max(max(row) for row in dp)


A = [1,2,3,4,5]
lenLongestFibSubseq(A)




