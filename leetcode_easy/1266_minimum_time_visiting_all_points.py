from typing import List


class Cord:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def manhattan_distance(self, other):
        return abs(self.x - other.x) + abs(self.y - other.y)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return "{} {}".format(self.x, self.y)


def make_move(current: Cord, target: Cord):
    min_dist = float('inf')
    min_result = None
    for option in [
        Cord(current.x + 1, current.y),
        Cord(current.x - 1, current.y),
        Cord(current.x, current.y + 1),
        Cord(current.x, current.y - 1),
        Cord(current.x + 1, current.y + 1),
        Cord(current.x - 1, current.y - 1)
    ]:
        if option.manhattan_distance(target) < min_dist:
            min_result = option
            min_dist = option.manhattan_distance(target)
    return min_result


class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        start = Cord(points[0][0], points[0][0])
        target = Cord(points[1][0], points[1][1])
        others = points[2:]
        counter = 0
        while start != target or len(others) > 0:
            if start == target:
                start = target
                new_data = others.pop(0)
                target = Cord(new_data[0], new_data[1])
            counter += 1
            start = make_move(start, target)
        return counter


class SolutionSimple:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        steps = 0
        for i in range(len(points) - 1):
            steps += max(abs(points[i + 1][1] - points[i][1]),
                     abs(points[i + 1][0] - points[i][0]))
        return steps

if __name__ == '__main__':
    SolutionSimple().minTimeToVisitAllPoints([[1, 1], [3, 4], [-1, 0]])

    Solution().minTimeToVisitAllPoints([[3, 2], [-2, 2]])