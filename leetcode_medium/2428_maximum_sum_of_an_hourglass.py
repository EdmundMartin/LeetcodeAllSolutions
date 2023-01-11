from typing import List


def hour_glass_sum(grid, row, col) -> int:
    cords = [
        (row - 1, col), (row -1, col -1), (row - 1, col + 1),
        (row, col),
        (row + 1, col - 1), (row + 1, col), (row + 1, col + 1)
    ]

    for r, c in cords:
        if r < 0 or r >= len(grid):
            return 0
        if c < 0 or c >= len(grid[0]):
            return 0
    total = 0
    for r, c in cords:
        total += grid[r][c]
    return total


class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:

        max_val = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                max_val = max(hour_glass_sum(grid, row, col), max_val)
        return max_val


if __name__ == '__main__':
    res = Solution().maxSum([[6,2,1,3],[4,2,1,5],[9,2,8,7],[4,1,2,9]])
    print(res)