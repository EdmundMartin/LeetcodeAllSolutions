from typing import List
from collections import defaultdict


class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:

        num_arrays = len(nums)
        counter = defaultdict(int)
        for arr in nums:
            for num in arr:
                counter[num] += 1

        return sorted([k for k in counter.keys() if counter[k] == num_arrays])