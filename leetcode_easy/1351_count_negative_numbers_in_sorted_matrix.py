from typing import List


# Runtime: 121 ms, faster than 98.06% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
# Memory Usage: 15 MB, less than 77.33% of Python3 online submissions for Count Negative Numbers in a Sorted Matrix.
class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        row, col = 0, len(grid[0]) - 1
        total = 0
        while row < len(grid) and col >= 0:
            pos = grid[row][col]
            if pos < 0 and col > 0:
                col -= 1
            else:
                if pos < 0:
                    idx = len(grid[0]) - col
                else:
                    idx = len(grid[0]) - 1 - col
                total += idx
                row += 1
        return total



if __name__ == '__main__':
    example_one = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]
    result = Solution().countNegatives(example_one)
    print(result)