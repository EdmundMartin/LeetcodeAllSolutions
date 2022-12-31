from typing import List


# Beats 98.26% on speed
class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        start = 0
        smallest = 0
        for num in nums:
            start = start + num
            smallest = min(start, smallest)
        if smallest >= 0:
            return 1
        return abs(smallest) + 1


if __name__ == '__main__':
    Solution().minStartValue([-3, 2, -3, 4, 2])