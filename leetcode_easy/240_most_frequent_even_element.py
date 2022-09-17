from typing import List


class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        most_common = None
        most_common_count = 0
        counter = {}
        for num in nums:
            if num % 2 == 0:
                result = counter.get(num, 0) + 1
                if result > most_common_count or result == most_common_count and num < most_common:
                    most_common = num
                    most_common_count = result
                counter[num] = result
        return -1 if most_common is None else most_common