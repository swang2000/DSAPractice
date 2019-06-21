
import collections
def updateMatrix(A):
    R, C = len(A), len(A[0])

    def neighbors(r, c):
        for cr, cc in ((r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)):
            if 0 <= cr < R and 0 <= cc < C:
                yield cr, cc

    q = collections.deque([((r, c), 0)
                           for r in range(R)
                           for c in range(C)
                           if A[r][c] == 0])
    seen = {x for x, _ in q}
    ans = [[0] * C for _ in A]
    while q:
        (r, c), depth = q.popleft()
        ans[r][c] = depth
        for nei in neighbors(r, c):
            if nei not in seen:
                seen.add(nei)
                q.append((nei, depth + 1))

    return ans


a = [[0,0,0],
    [0,1,0],
    [1,1,1]]

updateMatrix(a)