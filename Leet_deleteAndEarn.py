import collections
def deleteAndEarn(nums):
    points, prev, curr = collections.Counter(nums), 0, 0
    for value in range(10001):
        prev, curr = curr, max(prev + value * points[value], curr)
    return curr


nums = [2, 2, 3, 3, 3, 4]
deleteAndEarn(nums)
