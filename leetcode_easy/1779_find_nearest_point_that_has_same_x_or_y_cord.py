from typing import List


# Runtime: 762 ms, faster than 89.55% of Python3 online submissions for Find Nearest Point That Has the Same X or Y Coordinate.
# Memory Usage: 19.2 MB, less than 93.63% of Python3 online submissions for Find Nearest Point That Has the Same X or Y Coordinate.
class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:
        result = float('inf')
        ret_idx = -1
        for idx, point in enumerate(points):
            curr_x, curr_y = point
            if curr_x == x or curr_y == y:
                manhattan_distance = abs(x - curr_x) + abs(y - curr_y)
                if manhattan_distance < result:
                    result = manhattan_distance
                    ret_idx = idx
        return ret_idx


if __name__ == '__main__':
    Solution().nearestValidPoint(3, 4, [[1,2],[3,1],[2,4],[2,3],[4,4]])