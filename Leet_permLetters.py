def letterCasePermutation(S):
    """
    :type S: str
    :rtype: List[str]
    """
    out = []

    def perm(S, chosen=''):
        if not S:
            out.append(chosen)
            return
        i = 0
        while i < len(S) and S[i].isdigit():
            chosen += S[i]
            i += 1
        if i < len(S):
            perm(S[i + 1:], chosen + S[i].upper())
            perm(S[i + 1:], chosen + S[i].lower())
        else:
            perm('', chosen)


    perm(S)
    return out

letterCasePermutation('a1b2')