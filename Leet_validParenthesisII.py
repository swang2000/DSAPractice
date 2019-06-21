def isValid(s):
    """
    :type s: str
    :rtype: bool
    """

    if len(s)%2 !=0: return False
    l, r = 0, len(s)-1
    while l<r:
        if s[l]=='(' and s[r]!=')':
            return False
        elif s[l]=='[' and s[r]!=']':
            return False
        elif s[l]=='{' and s[r]!='}':
            return False
        l += 1
        r -= 1
    return True

isValid("()[]{}")
