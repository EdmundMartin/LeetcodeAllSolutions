from typing import List


class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        seen = dict()
        for num in nums:
            if num in seen:
                seen[num] += 1
            else:
                seen[num] = 1

        return sum([k for k, v in seen.items() if v == 1])
