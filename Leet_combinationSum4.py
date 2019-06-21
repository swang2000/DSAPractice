def combinationSum4(nums, target):
    out = [0] * (target + 1)
    for i in range(1, target + 1):

        for j in nums:
            if i - j > 0:
                out[i] += out[i - j]
            elif i==j:
                out[i] += 1
    return out[-1]


nums = [1, 2, 3]
target = 4

combinationSum4(nums, target)