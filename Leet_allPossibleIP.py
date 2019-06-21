def restoreIpAddresses(s):
    """
    :type s: str
    :rtype: List[str]
    """

    def bt(start, current):
        if len(current) == 4:
            if start == len(s):
                result.append('.'.join(current))
            return
        for i in range(start + 1, min(start + 4, len(s) + 1)):
            if i - 1 > start and s[start] == '0':
                continue
            a = s[start:i]
            if 0 <= int(a) <= 255:
                current.append(a)
                bt(i, current)
                current.pop()

    result = []
    bt(0, [])
    return result


restoreIpAddresses('25525511135')