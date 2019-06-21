# def subsets(nums):
#     if not nums: return []
#     path, result = [], []
#     nums.sort()
#     DFS(nums, 0, path, result)
#     return result
#
#
# def DFS(nums, start, path, result):
#     result.append(path[:])  # add path to result every time
#     for i in range(start, len(nums)):
#         DFS(nums, i + 1, path + [nums[i]], result)


def subsets(nums):
    output = []

    def f(nums, s, i):
        if len(s) == i:
            output.append(s[:])
            return

        for j in range(len(nums)):
            f(nums[j + 1:], s + [nums[j]], i)

    for i in range(len(nums) + 1):
        f(nums, [], i)
    return output


subsets([1,2,3,])