class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        self.r, self.c = len(board), len(board[0])
        border = set(list(zip(range(self.c), [0] * self.c)) + list(zip(range(self.c), [self.r - 1] * self.c)) + list(zip([0] * self.r, range(self.r))) + list(
            zip([self.c - 1] * self.r, range(self.r))))
        zeros = [(y, x) for x, y in border if board[y][x] == 'O']
        self.seen, self.out = set(), []
        self.res = [['X']*self.c for _ in range(self.r)]
        for x, y in zeros:
            self.bfs(board, x, y)
        for x,y in self.out:
            self.res[x][y] ='O'


    def bfs(self, board, x, y):
        if (x, y) not in self.seen and board[x][y] == 'O':
            self.seen.add((x, y))
            self.out.append((x,y))
            if x-1 >0 and 0< y < self.c-1:
                self.bfs(board, x-1, y)
            if x+1 <self.r -1 and 0< y < self.c-1:
                self.bfs(board, x+1, y)
            if y-1 >0 and 0< x < self.r-1:
                self.bfs(board, x, y-1)
            if y+1 <self.c-1 and 0< x < self.r-1:
                self.bfs(board, x, y+1)






board = [["X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X","X"],["X","X","X","X","X","X","X","X","X","O","O","O","X","X","X","X","X","X","X","X"],["X","X","X","X","X","O","O","O","X","O","X","O","X","X","X","X","X","X","X","X"],["X","X","X","X","X","O","X","O","X","O","X","O","O","O","X","X","X","X","X","X"],["X","X","X","X","X","O","X","O","O","O","X","X","X","X","X","X","X","X","X","X"],["X","X","X","X","X","O","X","X","X","X","X","X","X","X","X","X","X","X","X","X"]]
mark = Solution()
mark.solve(board)
mark.res

