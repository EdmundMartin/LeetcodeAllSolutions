from typing import List
from collections import defaultdict


class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        original_idx = defaultdict(int)
        for idx, num in enumerate(nums):
            original_idx[num] = idx
        nums = sorted(nums)
        if nums[-1] >= nums[-2] * 2:
            return original_idx[nums[-1]]
        return -1


if __name__ == '__main__':
    res = Solution().dominantIndex([3, 6, 1, 0])
    print(res)