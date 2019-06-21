import collections, heapq
class Solution(object):
    # def findCheapestPrice(self, n, flights, src, dst, K):
    #     """
    #     :type n: int
    #     :type flights: List[List[int]]
    #     :type src: int
    #     :type dst: int
    #     :type K: int
    #     :rtype: int
    #     """
    #     self.costs = []
    #     self.seen = set()
    #     self.fmap = collections.defaultdict(list)
    #     for x in flights:
    #         self.fmap[x[0]].append(x[1:])
    #     self.bfs(src, dst, K, 0)
    #     if len(self.costs) > 0:
    #         return min(self.costs)
    #     else:
    #         return -1
    #
    # def bfs(self, x, dst, k, cost):
    #     a = [c[0] for c in self.fmap[x]]
    #     if k >= 0 and a:# and x not in self.seen:
    #         self.seen.add(x)
    #         for c in self.fmap[x]:
    #             if c[0] == dst:
    #                 self.costs.append(cost + c[1])
    #             else:
    #                 self.bfs(c[0], dst, k - 1, cost + c[1])
    #     return


    def findCheapestPrice(self, n, flights, src, dst, K):
        """
        :type n: int
        :type flights: List[List[int]]
        :type src: int
        :type dst: int
        :type K: int
        :rtype: int
        """

        f = collections.defaultdict(dict)
        for a, b, p in flights:
            f[a][b] = p
        heap = [(0, src, K + 1)]
        while heap:
            p, i, k = heapq.heappop(heap)
            if i == dst:
                return p
            if k > 0:
                for j in f[i]:
                    heapq.heappush(heap, (p + f[i][j], j, k - 1))
        return -1


n = 10
flights = [[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]]
s = Solution()
s.findCheapestPrice(n, flights, 6, 0, 7)
