def minAddToMakeValid(S):
    """
    :type S: str
    :rtype: int
    """
    stack = []
    for c in S:
        if not stack or c == '(':
            stack.append(c)
        elif c == ')' and stack[-1] == '(':
            stack.pop()
    return len(stack)


minAddToMakeValid("()))((")