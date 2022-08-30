from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mapping = {}
        for current_idx, num in enumerate(nums):
            if num in mapping:
                idx = mapping[num]
                if abs(current_idx - idx) <= k:
                    return True
                mapping[num] = current_idx
            else:
                mapping[num] = current_idx
        return False
