def removeElement(nums, val):
    if len(nums) == 0:
        return 0
    else:
        i = 0
        while i < len(nums):
            if val == nums[i]:
                nums.pop(i)
            else:
                i += 1
        return len(nums)

nums = [3,2,2,3]
removeElement(nums, 3)