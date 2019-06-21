
import collections
def exist(board, word):
    cmap = collections.defaultdict(list)
    for c in word:
        cmap[c].append([(x, y) for x in range(len(board)) for y in range(len(board[0])) if board[x][y] == c])
    for i, v in cmap.items():
        cmap[i] = v[0]

    m = len(board) * len(board[0])
    def bfs(d, seen):
        if len(d)==1 and any(x not in seen for x in cmap[d[0]]) and len(seen) < m: return True
        elif len(d)==1: return False
        for x, y in cmap[d[0]]:

            next = cmap[d[1]]
            n = len(seen)
            for t in next:
                if t not in seen and t in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                    seen.append((x,y))
                    return bfs(d[1:], seen)
            seen = seen[:n]

        return False

    return bfs(word, [])

board = [["a","a"]]

word = "aaa"

exist(board, word)