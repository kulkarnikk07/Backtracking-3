# Backtracking-3

## Problem 1 N Queens(https://leetcode.com/problems/n-queens/)

result = []
    def solveNQueens(self, n):
        self.result = []
        grid = [[0 for i in range(n)] for j in range(n)]
        self.backtrack(grid, 0)
        return self.result

    def backtrack(self, grid, r):
        # base
        if r == len(grid):
            res = []
            for i in range(len(grid)):
                li = ""
                for j in range(len(grid)):
                    if grid[i][j] == 0:
                        li += "."
                    else:
                        li += "Q"
                res.append(li)
            self.result.append(res)
        # action
        for c in range(len(grid)):
            if self.is_safe(r, c, grid):
                grid[r][c] = 1
                # backtrack
                self.backtrack(grid, r+1)
                #recurse
                grid[r][c] = 0

    def is_safe(self,r, c, grid):
        # check col up
        for i in range(r):
            if grid[i][c] == 1:
                return False
        # diagonal top left
        i, j = r, c
        while i >= 0 and j >= 0:
            if grid[i][j] == 1:
                return False
            i -= 1
            j -= 1
        # diagonal top right
        i, j = r, c
        while i >= 0 and j < len(grid):
            if grid[i][j] == 1:
                return False
            i -= 1
            j += 1
        return True

## Problem 2 Word Search(https://leetcode.com/problems/word-search/)

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if board == None or len(board) == 0:
            return []
        self.m = len(board)
        self.n = len(board[0])
        self.Dirs =[[-1,0],[1,0],[0,-1],[0,1]] #UDLR 
        for i in range(self.m):
            for j in range(self.n):
                if board[i][j] == word[0]:
                    if self.backtrack(board,i,j, word,0) == True:
                        return True
        return False

    def backtrack(self, board: List[List[str]], row: int, col: int, word:str, index: int)-> bool:
        #base
        if index == len(word):
            return True
        if row<0 or row == self.m or col<0 or col == self.n or board[row][col] == '#':
            return False

        #logic
        if board[row][col] == word[index]:
            storage = board[row][col]
            board[row][col] = '#'
            for Dir in self.Dirs:
                nr = row + Dir[0]
                nc = col + Dir[1]
                if self.backtrack(board, nr, nc, word, index+1) == True:
                    return True
            board[row][col] = storage
        return False
