from typing import List


# Runtime: 66 ms, faster than 91.18% of Python3 online submissions for Two Sum.
# Memory Usage: 15.2 MB, less than 50.28% of Python3 online submissions for Two Sum.
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}

        for idx, value in enumerate(nums):
            other = target - value
            if other in seen:
                return [seen[other], idx]
            seen[value] = idx
        return []
