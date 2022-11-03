from typing import List

class Solution:
    def findMaxK(self, nums: List[int]) -> int:

        mapping = {}
        max_found = -1
        for num in nums:
            abs_num = abs(num)
            if abs_num not in mapping:
                mapping[abs_num] = 1 if num > 0 else -1
            if abs_num in mapping:
                if num > 0 and mapping[abs_num] < 0:
                    max_found = max(abs_num, max_found)
                elif num < 0 and mapping[abs_num] > 0:
                    max_found = max(abs_num, max_found)
        return max_found