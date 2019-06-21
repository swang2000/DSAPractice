def removeDuplicates(nums):
    if nums:
        x = nums[0]
    else:
        return 0
    i = 1
    while i < len(nums):
        if x == nums[i]:
            nums.remove(nums[i])
        else:
            x = nums[i]
            i = i +1
    return len(nums)

nums = [0,0,1,1,1,2,2,3,3,4]
removeDuplicates(nums)
