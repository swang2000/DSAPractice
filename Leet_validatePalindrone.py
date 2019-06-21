def validPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    n = len(s)
    if s == s[-1::-1]:
        return True
    else:
        for i in range(n):
            temp = (s[:i] + s[i + 1:])
            if temp == temp[-1::-1]:
                return True
    return False


validPalindrome('abca')