def countPrime(n):
    pl = [True]*n
    if n <1:
        return False
    pl[0] = False
    for i in range(3,n):
        for j in range(2, i):
            if i % j ==0:
                pl[i-1] = False
                break
    return sum(pl)

countPrime(10)