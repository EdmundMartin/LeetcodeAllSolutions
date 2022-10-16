from typing import List


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        mapping = {}

        for num in nums2:
            while stack and num > stack[-1]:
                mapping[stack.pop()] = num
            stack.append(num)

        while stack:
            mapping[stack.pop()] = -1

        results = []
        for num in nums1:
            results.append(mapping.get(num))
        return results