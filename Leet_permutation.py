
def permute(nums):
    output = []
    def perm(nums, s):
        if not nums:
            output.append(s)

        else:
            for i in range(len(nums)):

                perm(nums[:i]+nums[i+1:], s+[nums[i]])

    perm(nums, [])
    return output

permute([1,2,3])

