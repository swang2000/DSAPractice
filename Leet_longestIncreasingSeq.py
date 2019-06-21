import collections
def lengthOfLIS(nums):
    """
    :type nums: List[int]
    :rtype: int
    """


    q = [1] * len(nums)
    if len(nums) == 0: return 0

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                q[i] = max(q[i], q[j] + 1)
    return max(q)


lengthOfLIS([1,3,6,7,9,4,10,5,6])