from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for val in nums:
            if val in seen:
                return True
            seen.add(val)
        return False


class SolutionAlternative:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        for i in range(1, len(nums)):
            prev = nums[i - 1]
            current = nums[i]
            if prev == current:
                return True
        return False
