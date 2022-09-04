from typing import List, Set


def search_island(grid, island_cords, seen: Set):
    if island_cords in seen:
        return 0, set()
    stack = [island_cords]
    unique_island = set()
    unique_island.add(island_cords)
    while stack:
        cords = stack.pop()
        for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            new_cords = (cords[0] + direction[0], cords[1] + direction[1])
            if new_cords[0] < 0 or new_cords[0] >= len(grid):
                continue
            if new_cords[1] < 0 or new_cords[1] >= len(grid[0]):
                continue
            if grid[new_cords[0]][new_cords[1]] == "1" and new_cords in seen:
                return 0, set()
            if grid[new_cords[0]][new_cords[1]] == "1" and new_cords not in unique_island:
                unique_island.add(new_cords)
                stack.append(new_cords)
    return 1, unique_island


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        total = 0
        seen = set()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    result, cords = search_island(grid, (i,j ), seen)
                    for cor in cords:
                        seen.add(cor)
                    total += result
        return total


if __name__ == '__main__':
    grid_one = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
    res = Solution().numIslands(grid_one)
    print(res)

    grid_two = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
    res = Solution().numIslands(grid_two)
    print(res)