def backspaceCompare(S, T):
    """
    :type S: str
    :type T: str
    :rtype: bool
    """
    s = []
    t = []
    for i in S:

        if i != '#':
            s.append(i)
        else:
            if len(s) > 0:
                s.pop()
    for i in T:

        if i != '#':
            t.append(i)
        else:
            if len(t) > 0:
                t.pop()
    return ''.join(s) ==''.join(t)


backspaceCompare("isfcow#", "isfco#w#")
