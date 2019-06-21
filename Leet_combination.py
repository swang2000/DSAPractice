def combinationSum(candidates, target):
    candidates.sort()
    dp = [[[]]] + [[] for i in range(target)]
    for i in range(1, target + 1):
        for number in candidates:
            if number > i: break
            for L in dp[i - number]:
                if not L or number >= L[-1]: dp[i] += L + [number],
    return dp[target]


candidates = [2,3,6,7]
target = 7
combinationSum(candidates, target)