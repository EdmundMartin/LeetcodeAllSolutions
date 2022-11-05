from typing import List



class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:

        nums.sort()
        pairs = 0

        for i in range(len(nums)):
            j = len(nums) - 1
            while i < j:
                if abs(nums[j] - nums[i]) > k:
                    j -= 1
                elif abs(nums[j] - nums[i]) == k:
                    j -= 1
                    pairs += 1
                else:
                    i += 1
        return pairs