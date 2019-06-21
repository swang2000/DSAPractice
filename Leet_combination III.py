def combinationSum3(k, n):
    # nums = list(range(1, 10))
    # out = []
    #
    # def bk(nums, k, n, l):
    #     if n == 0 and k == 0:
    #         out.append(l)
    #         return True
    #     elif k <= 0 or n <= 0:
    #         return False
    #     elif nums:
    #         for x in nums:
    #             if bk([i for i in nums if i!=x], k - 1, n - x, l + [x]):
    #                 bk([i for i in nums if i!=x], k - 1, n - x, l + [x])
    #     else:
    #         return False
    #
    # bk(nums, k, n, [])
    # return out
    def combine(k, n):
        res = [[]]
        for i in range(1, 10):
            res += [[i] + x for x in res if len(x) < k and sum(x) < n]
        return [x for x in res if len(x) == k and sum(x) == n]

    combine(k, n)


combinationSum3(3, 7)