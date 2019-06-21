
def combinationSum2(candidates, target):
    candidates.sort()
    dp = [None] + [set() for _ in range(target)]
    for i in candidates:
        if i > target: break
        for j in range(target-i, 0, -1):
            dp[i+j] |= {x + (i,) for x in dp[j]}
        dp[i].add((i,))
    return map(list, dp[target])

candidates = [10,1,2,7,6,1,5] #map(list,
target = 8

combinationSum2(candidates, target)
