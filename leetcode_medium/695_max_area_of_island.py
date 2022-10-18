from typing import List


def island_size(grid, x, y, seen):
    seen.add((x, y))
    queue = [(x, y)]

    area = 0
    while queue:
        current_x, current_y = queue.pop(0)
        if current_x < 0 or current_x >= len(grid):
            continue
        if current_y < 0 or current_y >= len(grid[0]):
            continue

        if grid[current_x][current_y] == 1:
            area += 1
            grid[current_x][current_y] = 0
            for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                new_x, new_y = current_x + direction[0], current_y + direction[1]
                if (new_x, new_y) not in seen:
                    queue.append((new_x, new_y))
                    seen.add((new_x, new_y))
    return area


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        seen = set()
        biggest = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    area = island_size(grid, row, col, seen)
                    biggest = max(area, biggest)
        return biggest


if __name__ == '__main__':
    t = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
     [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
     [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
     [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]

    result = Solution().maxAreaOfIsland(t)
    print(result)