from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        output = [0] * len(nums)
        output[0] = nums[0]
        for idx, num in enumerate(nums[1:]):
            output[idx+1] = num + output[idx]
        return output