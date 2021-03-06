import bisect
class Solution:
    def __init__(self, N):
        self.N, self.L = N, []

    def seat(self):
        N, L = self.N, self.L
        if not L: res = 0
        else:
            d, res = L[0], 0
            for a, b in zip(L, L[1:]):
                if (b - a) // 2 > d:
                    d, res = (b - a) // 2, (b + a) // 2
            if N - 1 - L[-1] > d: res = N - 1
        bisect.insort(L, res)
        return res

    def leave(self, p):
        self.L.remove(p)

exam = Solution(10)
exam.seat()
exam.seat()
exam.seat()
exam.seat()
exam.leave(4)
exam.seat()


