from typing import List, Dict, Tuple


SolutionGrid = List[List[List]]


def paths(solutions: Dict, row: int, col: int, depth: int):

    # Grid is four rows - with three coulmns - final column only one valid location
    if row < 0 or col < 0 or row >= 4 or col >= 3 or (row == 3 and col != 1):
        return 0

    if depth == 1:
        return 1

    if (depth, row, col) in solutions:
        return solutions[(depth, row, col)]

    power = pow(10, 9) + 7
    new_depth = depth - 1

    solutions[(depth, row, col)] = (
        paths(solutions, row - 1, col - 2, new_depth) % power +
        paths(solutions, row - 2, col - 1, new_depth) % power +
        paths(solutions, row - 2, col + 1, new_depth) % power +
        paths(solutions, row - 1, col + 2, new_depth) % power +
        paths(solutions, row + 1, col + 2, new_depth) % power +
        paths(solutions, row + 2, col + 1, new_depth) % power +
        paths(solutions, row + 2, col - 1, new_depth) % power +
        paths(solutions, row + 1, col - 2, new_depth) % power
    )
    return solutions[(depth, row, col)]


class Solution:

    def __init__(self):
        self.max = pow(10, 9) + 7

    def knightDialer(self, n: int) -> int:

        solutions = {}
        result = 0
        for i in range(4):
            for j in range(3):
                result = result + paths(solutions, i, j, n) % self.max
        return result