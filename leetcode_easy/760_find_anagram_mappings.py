from typing import List


class Solution:
    def anagramMappings(self, nums1: List[int], nums2: List[int]) -> List[int]:
        second_mapping = dict()
        for idx, val in enumerate(nums2):
            second_mapping[val] = idx
        result = []
        for num in nums1:
            result.append(second_mapping[num])
        return result