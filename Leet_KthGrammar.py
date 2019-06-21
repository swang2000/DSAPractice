def kthGrammar(N, K):
    """
    :type N: int
    :type K: int
    :rtype: int
    """
    bits = []
    bits.append('0')
    bits.append('01')
    for i in range(2, N):
        comp = ''.join(['1' if x == '0' else '0' for x in bits[i - 1]])
        bits.append(bits[i - 1] + comp)
    return int(bits[N - 1][K-1])


kthGrammar(30,5)
