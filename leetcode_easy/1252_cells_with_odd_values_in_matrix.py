from typing import List
from collections import defaultdict


class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        rows = m
        cols = n
        matrix = defaultdict(int)
        odd_values = set()
        for move in indices:
            for col in range(cols):
                if (move[0], col) in odd_values:
                    odd_values.remove((move[0], col))
                matrix[(move[0], col)] += 1
                if matrix[(move[0], col)] % 2 != 0:
                    odd_values.add((move[0], col))
            for row in range(rows):
                if (row, move[1]) in odd_values:
                    odd_values.remove((row, move[1]))
                matrix[(row, move[1])] += 1
                if matrix[(row, move[1])] % 2 != 0:
                    odd_values.add((row, move[1]))
        return len(odd_values)


if __name__ == '__main__':
    res = Solution().oddCells(2, 3, [[0, 1], [1, 1]])
    print(res)

    res = Solution().oddCells(2, 2, [[1, 1], [0, 0]])
    print(res)