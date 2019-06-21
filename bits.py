def reverse(x):
    """
    :type x: int
    :rtype: int
    """
    if x > 0:
        x = int(str(x)[::-1])

    if x < 0:
        x = -1 * int(str(x * (-1))[::-1])

    if (x > pow(2, 31) - 1) or (x < -1 * pow(2, 31)):
        return 0
    return x

reverse(-120)


