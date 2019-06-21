def rotate(nums, k):
    """
    Do not return anything, modify nums in-place instead.
    """
    nums = nums[(len(nums) - k):] + nums[:(len(nums) - k)]


nums = [1,2,3,4,5,6,7]
rotate(nums, 3)