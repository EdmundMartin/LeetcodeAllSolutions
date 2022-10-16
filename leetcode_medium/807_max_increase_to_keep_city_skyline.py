from typing import List


class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        grid_size = len(grid)
        row_maxes = [-1] * grid_size
        col_maxes = [-1] * grid_size

        for r in range(grid_size):
            for c in range(grid_size):
                row_maxes[r] = max(row_maxes[r], grid[r][c])
                col_maxes[c] = max(col_maxes[c], grid[r][c])

        answer = 0
        for r in range(grid_size):
            for c in range(grid_size):
                answer += min(row_maxes[r], col_maxes[c]) - grid[r][c]
        return answer
