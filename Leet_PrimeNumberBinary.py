def countPrimeSetBits(L, R):
    return sum(665772 >> bin(i).count('1') & 1 for i in range(L, R+1))



countPrimeSetBits(6, 10)