from typing import List


# Beats 88.67% of solutions
class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        total = 0

        for r in grid:
            r.sort()

        while len(grid[0]) > 0:
            current_max = -1
            for r in grid:
                current_max = max(r[-1], current_max)
                r.pop(-1)
            total += current_max
        return total


if __name__ == '__main__':
    Solution().deleteGreatestValue([[1, 2, 4], [3, 3, 1]])
