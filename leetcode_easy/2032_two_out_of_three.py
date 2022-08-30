from typing import List


# Runtime: 79 ms, faster than 90.89% of Python3 online submissions for Two Out of Three.
# Memory Usage: 13.9 MB, less than 38.54% of Python3 online submissions for Two Out of Three.
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        results = dict()
        for arr in [nums1, nums2, nums3]:
            sub_dict = {}
            for num in arr:
                if num not in sub_dict:
                    current_val = results.get(num, 0)
                    results[num] = current_val + 1
                    sub_dict[num] = 1
        return_val = []
        for key, value in results.items():
            if value >= 2:
                return_val.append(key)
        return return_val