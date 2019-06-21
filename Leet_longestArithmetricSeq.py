def longestArithSeqLength(A):
    dp = {}
    for i in range(len(A)):
        for j in range(i + 1, len(A)):
            dp[j, A[j] - A[i]] = dp.get((i, A[j] - A[i]), 1) + 1
    return max(dp.values())

A = [9,4,7,2,10]
longestArithSeqLength(A)
