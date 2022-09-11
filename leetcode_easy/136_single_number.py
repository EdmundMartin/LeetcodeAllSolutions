from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        seen = {}
        for num in nums:
            if num not in seen:
                seen[num] = 1
            else:
                seen[num] += 1
        for ch, val in seen.items():
            if val == 1:
                return ch