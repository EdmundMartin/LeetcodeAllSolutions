from typing import List


class Solution:
    def isConsecutive(self, nums: List[int]) -> bool:
        expected = set([i for i in range(min(nums), max(nums) + 1)])
        for num in nums:
            if num not in expected:
                return False
            expected.remove(num)
        return len(expected) == 0



class SolutionSlower:
    def isConsecutive(self, nums: List[int]) -> bool:
        nums = sorted(nums)
        idx = 1
        while idx < len(nums):
            if nums[idx] - nums[idx - 1] != 1:
                return False
            idx += 1
        return True


if __name__ == '__main__':
    Solution().isConsecutive([1, 3])