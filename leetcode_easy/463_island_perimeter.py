from typing import List


def check_adjacent(grid, row, col) -> int:
    count = 0
    for cord in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
        new_row, new_col = cord[0] + row, cord[1] + col
        if new_row < 0 or new_col < 0:
            count += 1
        elif new_row >= len(grid) or new_col >= len(grid[0]):
            count += 1
        elif grid[new_row][new_col] != 1:
            count += 1
    return count


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        total = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    total += check_adjacent(grid, i, j)
        return total


if __name__ == '__main__':
    test_array = Solution().islandPerimeter([[0,1,0,0],[1,1,1,0],[0,1,0,0],[1,1,0,0]])
    print(test_array)

    test_two = Solution().islandPerimeter([[1, 0]])
    print(test_two)