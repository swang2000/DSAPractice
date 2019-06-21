def isHappy(n: int):
    m = list(map(int, list(str(n))))
    while len(m) > 1:
        x = sum([k*k for k in m])

        m = list(map(int, list(str(x))))
    return True
    return False


isHappy(2)