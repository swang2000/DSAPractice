def nextPermutation(nums):
    """
    :type nums: List[int]
    :rtype: None Do not return anything, modify nums in-place instead.
    """

    i = len(nums) - 1
    j = i - 1
    flag = False
    while j >= 0:
        if nums[i] > nums[j]:
            nums[i], nums[j] = nums[j], nums[i]
            nums = nums[:j + 1] + sorted(nums[j + 1:])
            flag = True
            break
        j -= 1

    if not flag: nums.sort()
    return nums

nextPermutation([1,3,2])