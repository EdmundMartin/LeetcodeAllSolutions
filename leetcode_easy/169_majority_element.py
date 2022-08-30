from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority = len(nums) // 2 + 1
        seen = dict()
        for value in nums:
            if value not in seen:
                seen[value] = 0
            seen[value] += 1
            if seen[value] >= majority:
                return value
        return -1
