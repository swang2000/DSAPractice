def subsetsWithDup(nums):
    output = set()
    s = [str(i) for i in nums]

    def f(s, temp, i):
        if len(temp) == i:
            output.add(temp)
            return
        for j in range(len(s)):
            f(s[j + 1:], temp + s[j], i)

    for i in range(len(s)+1):
        f(s, '', i)
    return [[int(i) for i in x] for x in output]


nums = [1,2,2]
subsetsWithDup(nums)
