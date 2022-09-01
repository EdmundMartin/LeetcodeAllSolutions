from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        seen_numbers = set(nums)
        for i in range(len(nums) + 1):
            if i not in seen_numbers:
                return i