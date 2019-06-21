def checkSubarraySum(nums, k):
    """
    :type nums: List[int]
    :type k: int
    :rtype: bool
    """
    if k == 0:
        return any(nums[i] == 0 and nums[i + 1] == 0 for i in range(len(nums) - 1))
    mods, cum_sum_mod_k = {0: -1}, 0
    for i, n in enumerate(nums):
        cum_sum_mod_k = (cum_sum_mod_k + n) % k
        if cum_sum_mod_k in mods and i - mods[cum_sum_mod_k] > 1:
            return True
        if cum_sum_mod_k not in mods:
            mods[cum_sum_mod_k] = i
    return False


nums = [23, 2, 6, 4, 7]
k =6
checkSubarraySum(nums, k)