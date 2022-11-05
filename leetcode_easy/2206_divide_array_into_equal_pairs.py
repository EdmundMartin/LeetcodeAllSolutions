from typing import List


class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        counter = {}

        for num in nums:
            if num in counter:
                counter[num] += 1
            else:
                counter[num] = 1
        for val in counter.values():
            if val % 2 != 0:
                return False
        return True