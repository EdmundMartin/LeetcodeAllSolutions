from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col = set()
        pos_diag = set()  # (r + c)
        neg_diag = set()  # (r - c)

        result = []
        board = [["."] * n for i in range(n)]

        def backtrack(r):
            if r == n:
                copy = [''.join(r) for r in board]
                result.append(copy)
                return
            for c in range(n):
                if c in col or (r + c) in pos_diag or (r-c) in neg_diag:
                    continue
                col.add(c)
                pos_diag.add(r + c)
                neg_diag.add(r - c)
                board[r][c] = "Q"
                backtrack(r + 1)

                col.remove(c)
                pos_diag.remove(r + c)
                neg_diag.remove(r - c)
                board[r][c] = "."
        backtrack(0)
        return result
