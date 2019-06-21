def reverseVowels(s):
    """
    :type s: str
    :rtype: str
    """
    l, r = 0, len(s) - 1
    t = list(s)
    pos = [i for i, x in enumerate(s) if x in ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']]
    while len(pos) > 1:
        t[pos[0]], t[pos[-1]] = t[pos[-1]], t[pos[0]]
        pos.pop(0)
        pos.pop(-1)
    return ''.join(t)


reverseVowels('aA')
