from functools import reduce

def integerBreak(n):
    """
    :type n: int
    :rtype: int
    """

    if n == 2:
        return 1
    if n == 3:
        return 2
    list_3 = [3] * int(n / 3)  # generate a list of 3
    mod_3 = n % 3
    if mod_3 == 1:  # if a 1 is left, then add it to the first element to get a 4
        list_3[0] += 1
    if mod_3 == 2:  # if a 2 is left, then put it into the list
        list_3.append(2)
    return reduce(lambda a, b: a * b, list_3, 1)


integerBreak(30)