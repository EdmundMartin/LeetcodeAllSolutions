from typing import List


class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:

        counter = {}
        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        candidates = [k for k, v in counter.items() if v == 1]
        return max(candidates) if len(candidates) > 0 else - 1
