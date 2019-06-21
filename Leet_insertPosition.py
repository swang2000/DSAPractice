def searchInsert(nums, target):
    n = len(nums)
    if nums[0] > target:
        return 0
    elif nums[-1] < target:
        return n
    l, h = 0, n - 1
    while l <= h:
        mid = (h + l) // 2
        if nums[mid] < target:
            l = mid + 1
        else:
            h = mid - 1
    return max(h,mid, l)



nums = [1, 3, 5, 6]
target = 2

searchInsert(nums, target)