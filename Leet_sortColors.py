def sortColors(nums):
    n = len(nums)
    l, r = 0, n-1
    for i in range(n):
        while nums[i] ==2 and i < r:
            nums[i], nums[r] = nums[r], nums[i]
            r -= 1
        while nums[i] == 0 and i > l:
            nums[i], nums[l] = nums[l], nums[i]
            l += 1
    return nums


nums = [1, 2, 1, 1, 0,0, 2]

sortColors(nums)
