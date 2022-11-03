from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        result = []
        for first, second in zip(nums[:n], nums[n:]):
            result.append(first)
            result.append(second)
        return result
