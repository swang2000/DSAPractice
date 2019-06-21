from collections import Counter

def removeDuplicateLetters(s):
    stack, used = [], set()
    count = Counter(s)
    for c in s:
        count[c] -= 1
        if c in used:
            continue
        while stack and count.get(stack[-1], 0) > 0 and stack[-1] > c:
            used.remove(stack.pop())
        stack.append(c)
        used.add(c)
    return "".join(stack)


removeDuplicateLetters("cbacdcbc")


def removeDuplicates(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if len(nums) < 2:
        return nums

    i = 1
    while i < len(nums):
        if nums[i - 1] == nums[i]:
            nums.remove(nums[i - 1])
            continue
        i += 1
    return nums


removeDuplicates([0,0,1,1,1,2,2,3,3,4])