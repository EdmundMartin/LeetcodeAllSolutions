from typing import List


class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        concat_length = len(nums) * 2
        result = [0] * concat_length
        for i in range(concat_length):
            result[i] = nums[i % len(nums)]
        return result
