
def search(nums, target):
    n = len(nums)
    l, h = 0, n - 1
    while l <= h:
        mid = (h + l) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            h = mid - 1
        else:
            l = mid + 1
    return -1


nums = [5]
target = 5
search(nums, target)
