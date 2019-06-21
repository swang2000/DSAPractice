def hasAlternatingBits(n):
    a = [x for i, x in enumerate(bin(n)[2:]) if i %2 ==0]
    b = [x for i, x in enumerate(bin(n)[2:]) if i %2 !=0]
    return all(x==a[0] for x in a) and all(x==b[0]  for x in b) and a[0] != b[0]


hasAlternatingBits(7)