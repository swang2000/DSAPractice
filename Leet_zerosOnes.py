def findMaxForm(strs, m, n):
    """
    :type strs: List[str]
    :type m: int
    :type n: int
    :rtype: int
    """
    table = {k: [[0] * (n + 1) for _ in range(m + 1)] for k in range(len(strs) + 1)}
    for i in range(1, len(strs) + 1):
        zeroes, ones = strs[i - 1].count('0'), strs[i - 1].count('1')
        for j in range(m + 1):
            for k in range(n + 1):
                if j >= zeroes and k >= ones:
                    table[i][j][k] = max(table[i - 1][j][k], 1 + table[i - 1][j - zeroes][k - ones])
                else:
                    table[i][j][k] = table[i - 1][j][k]
    return table[len(strs)][m][n]


strs = ["10", "0001", "111001", "1", "0"]
findMaxForm(strs, 5, 3)
