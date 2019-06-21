import math


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2: return 0
        cnt = [0] * max(n, 5)
        cnt[2], cnt[3], cnt[4] = 1, 2, 2
        if n >= 5:
            for i in range(5, n):
                if i % 2 == 0:
                    cnt[i] = cnt[i - 1]
                else:
                    if self.checkPrime(i):
                        cnt[i] = cnt[i - 1] + 1
                    else:
                        cnt[i] = cnt[i - 1]
        return cnt[n - 1]

    def checkPrime(self, i):
        j = 5
        return True


a = Solution()
a.countPrimes(10)