def nextGreaterElements(nums):
    """
    :type nums: List[int]
    :rtype: List[int]
    """
    # n = len(nums)
    # out = [-1] * n
    # for i, v in enumerate(nums):
    #     if i == n - 1:
    #         compare = nums
    #     else:
    #         compare = nums[i + 1:] + nums[:i]
    #     for a in compare:
    #         if a > v:
    #             out[i] = a
    #             break
    # return out

    cache, st = {}, []
    for idx, x in enumerate(nums):
        while st and st[-1][1] < x:
            a, b = st.pop()
            cache[a] = x
        st.append((idx, x))
    for idx, x in enumerate(nums):
        while st and st[-1][1] < x:
            a, b = st.pop()
            cache[a] = x
        st.append((idx, x))
    result = [-1] * len(nums)
    for idx, x in enumerate(nums):
        if idx in cache:
            result[idx] = cache[idx]
    return result


nextGreaterElements([1,2,1])