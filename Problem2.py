"""
Implemented referring to the solution
Time Complexity: O(M * N * 3^L)
Space Compelxity: O(M * N + L)
"""
class Solution:
    def __init__(self):
        self.dirs = [(0,1), (1,0), (-1,0), (0,-1)]
        self.m = 0
        self.n = 0

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.m = len(board)
        self.n = len(board[0])
        self.visited = [[False] * self.n for _ in range(self.m)]

        for i in range(self.m):
            for j in range(self.n):
                if self.dfs(board, word, i, j):
                    return True

        return False

    def dfs(self, board: List[List[str]], word: str, i: int, j: int) -> bool:
        # Base cases
        if i < 0 or i >= self.m or j < 0 or j >= self.n or self.visited[i][j]:
            return False

        if board[i][j] != word[0]:
            return False

        if len(word) == 1:
            return True

        # Mark the cell as visited
        self.visited[i][j] = True

        # Explore all 4 directions
        for dx, dy in self.dirs:
            r, c = i + dx, j + dy
            if self.dfs(board, word[1:], r, c):
                return True

        # Backtrack
        self.visited[i][j] = False
        return False