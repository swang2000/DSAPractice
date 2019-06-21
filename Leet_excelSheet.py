def convertToTitle(n):
    """
    :type n: int
    :rtype: str
    """
    out = []
    letters = [chr(s) for s in range(ord('A'), ord('Z')+1)]
    temp = n
    while temp>0:
        out.append(letters[(temp-1)%26])
        temp = (temp-1)//26
    out.reverse()
    return ''.join(out)

convertToTitle(701)



