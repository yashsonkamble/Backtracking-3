"""
Implemented referring to the solution
Time Complexity: O(N! * N^2)
Space Compelxity: O(N^2 + K * N^2)
"""
class Solution:
    def __init__(self):
        self.results = []

    def solveNQueens(self, n: int) -> List[List[str]]:
        board = [[0 for _ in range(n)] for _ in range(n)]
        self.placeQueens(board, 0, n)
        return self.results

    def placeQueens(self, board: List[List[int]], r: int, n: int) -> bool:
        # Base case
        if r == n:
            temp = []
            for i in range(n):
                row = ""
                for j in range(n):
                    if board[i][j] == 1:
                        row += 'Q'
                    else:
                        row += '.'
                temp.append(row)
            self.results.append(temp)
            return False

        # Recursive case
        for i in range(n):
            if self.isSafe(board, r, i, n):
                board[r][i] = 1
                if self.placeQueens(board, r + 1, n):
                    return True
                board[r][i] = 0  # Backtrack
        return False

    def isSafe(self, board: List[List[int]], i: int, j: int, n: int) -> bool:
        # Same column
        for r in range(i):
            if board[r][j] == 1:
                return False

        # Left diagonal
        x, y = i - 1, j - 1
        while x >= 0 and y >= 0:
            if board[x][y] == 1:
                return False
            x -= 1
            y -= 1

        # Right diagonal
        x, y = i - 1, j + 1
        while x >= 0 and y < n:
            if board[x][y] == 1:
                return False
            x -= 1
            y += 1

        return True