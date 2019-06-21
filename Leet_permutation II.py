def permuteUnique(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if not nums:
        return []

    ans = []

    def f(n, curr, l):
        if len(curr) == l:
            ans.append(curr)
            return

        visited = []

        for i in range(len(n)):
            if n[i] in visited:
                continue

            f(n[0:i] + n[i + 1:], curr + [n[i]], l)
            visited.append(n[i])

    f(nums, [], len(nums))

    return ans

nums = [1,1,2]
permuteUnique(nums)