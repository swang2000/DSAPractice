
from functools import reduce
def maxProduct(nums):
    """
    :type nums: List[int]
    :rtype: int
    """


    maximum = big = small = nums[0]
    for n in nums[1:]:
        big, small = max(n, n * big, n * small), min(n, n * big, n * small)
        maximum = max(maximum, big)
    return maximum
maxProduct([2,3,-2,4])