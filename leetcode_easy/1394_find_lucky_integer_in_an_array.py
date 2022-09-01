from typing import List


class Solution:
    def findLucky(self, arr: List[int]) -> int:
        result = -1
        counter = {}
        for num in arr:
            if num not in counter:
                counter[num] = 1
            else:
                counter[num] += 1
        lucky_nums = [k for k, v in counter.items() if k == v]
        if len(lucky_nums) == 0:
            return result
        return max(lucky_nums)
