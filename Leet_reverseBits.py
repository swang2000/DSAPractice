def reverseBits(n):
    origin = '{0.032b}'.format(n)
    a =origin[-1:]
    return int(a, 2)

reverseBits(25)
