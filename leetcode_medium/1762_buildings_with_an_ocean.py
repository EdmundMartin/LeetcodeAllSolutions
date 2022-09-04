from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        visible = [len(heights)-1]
        right_max = heights[-1]
        idx = len(heights) - 2
        while idx >= 0:
            if heights[idx] > right_max:
                visible = [idx] + visible
                right_max = heights[idx]
            idx -= 1
        return visible


class SolutionAlt:
    def findBuildings(self, heights: List[int]) -> List[int]:
        n = len(heights)
        answer = []
        max_height = -1

        for current in reversed(range(n)):
            if max_height < heights[current]:
                answer.append(current)
                max_height = heights[current]
        answer.reverse()
        return answer


if __name__ == '__main__':
    result = Solution().findBuildings([4, 2, 3, 1])
    print(result)