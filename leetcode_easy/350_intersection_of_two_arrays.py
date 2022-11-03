from typing import List
from collections import defaultdict


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:

        first = defaultdict(int)
        second = defaultdict(int)

        for num in nums1:
            first[num] += 1
        for num in nums2:
            second[num] += 1
        result = []
        for key, val in first.items():
            if second[key] != 0:
                for i in range(min(val, second[key])):
                    result.append(key)
        return result