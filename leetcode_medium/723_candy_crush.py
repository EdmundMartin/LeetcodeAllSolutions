from typing import List


class Solution:
    def candyCrush(self, board: List[List[int]]) -> List[List[int]]:
        rows = len(board)
        columns = len(board)
        crushed = False

        for r in range(rows):
            for c in range(columns - 2):
                num = abs(board[r][c])
                if abs(board[r][c]) == abs(board[r][c+1]) == abs(board[r][c+2]):
                    board[r][c] = num
                    board[r][c+1] = num
                    board[r][c+2] = num
                    crushed = True

        for r in range(rows-2):
            for c in range(columns):
                num = abs(board[r][c])
                if abs(board[r][c]) == abs(board[r+1][c]) == abs(board[r+2][c]):
                    board[r][c] = num
                    board[r+1][c] = num
                    board[r+2][c] = num
                    crushed = True

        if crushed:
            for col in range(columns):
                bottom_row = rows - 1
                for r in range(rows - 1, -1, -1):
                    if board[r][col] > 0:
                         board[bottom_row][col] = board[r][col]
                         bottom_row -= 1
                # fill top rows with 0s
                for top_row in range(bottom_row, -1, -1):
                    board[top_row][col] = 0
        return board if not crushed else self.candyCrush(board)