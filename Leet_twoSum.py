def twoSum(nums, target):
    maps = dict()
    for idx, v in enumerate(nums):
        maps[idx] = v
    for i in range(len(nums)):
        c = target - nums[i]
        a = [k for k, v in maps.items() if v == c]
        if len(a) == 1 and i != a[0]:
            return [i, a[0]]
        elif len(a) > 1:
            return [i, a[-1]]


twoSum([2,5,5,11], 10)