def minSteps(n):
    """
    :type n: int
    :rtype: int
    """

    if n == 1: return 0
    for i in range(2, n + 1):
        if n % i == 0:
            return minSteps(int(n / i))+ i



minSteps(9)