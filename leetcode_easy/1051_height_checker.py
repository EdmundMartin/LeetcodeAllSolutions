from typing import List


# Runtime: 40 ms, faster than 90.86% of Python3 online submissions for Height Checker.
# Memory Usage: 13.8 MB, less than 95.38% of Python3 online submissions for Height Checker.
class Solution:
    def heightChecker(self, heights: List[int]) -> int:

        copy = sorted(heights)

        count = 0
        for i in range(len(heights)):
            if copy[i] != heights[i]:
                count += 1
        return count
