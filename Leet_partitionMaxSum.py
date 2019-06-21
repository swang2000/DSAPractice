def maxSumAfterPartitioning(A, K):
    asum = [max(A[:i]) * len(A[:i]) for i in range(1, len(A) + 1)]
    for i in range(K, len(A)):
        pre = asum[i - K:i]
        new = A[i - K:i + 1]
        asum[i] = max([pre[i - 1] + max(new[i:]) * len(new[i:]) for i in range(1, len(new))])
    return asum[-1]



A= [1,15,7,9,2,5,10]
maxSumAfterPartitioning(A, 3)