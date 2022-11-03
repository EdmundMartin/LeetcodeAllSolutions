from typing import List


def calculate_box(row, col) -> int:
    return (row // 3) * 3 + col // 3


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        n = 9
        row_checks = [set() for _ in range(9)]
        col_checks = [set() for _ in range(9)]
        box_checks = [set() for _ in range(9)]

        for row in range(9):
            for col in range(9):
                val = board[row][col]
                if val == ".":
                    continue

                if val in row_checks[row]:
                    return False
                row_checks[row].add(val)

                if val in col_checks[col]:
                    return False
                col_checks[col].add(val)

                idx = (row // 3) * 3 + col // 3
                if val in box_checks[idx]:
                    return False
                box_checks[idx].add(val)
        return True