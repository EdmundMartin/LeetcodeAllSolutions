

class Solution:
    def totalNQueens(self, n: int) -> int:
        cols = set()
        pos_diag = set()  # (r + c)
        neg_diag = set()  # (r - c)

        result = []
        board = [["."] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                copy = [''.join(r) for r in board]
                result.append(copy)
                return
            for col in range(n):
                if col in cols or (r + col) in pos_diag or (r - col) in neg_diag:
                    continue
                cols.add(col)
                pos_diag.add(r + col)
                neg_diag.add(r - col)

                board[r][col] = "Q"

                backtrack(r + 1)

                cols.remove(col)
                pos_diag.remove(r + col)
                neg_diag.remove(r - col)
                board[r][col] = "."
        backtrack(0)
        return len(result)
