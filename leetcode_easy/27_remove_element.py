from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idx_without_target = 0
        for idx, num in enumerate(nums):
            if num != val:
                nums[idx_without_target] = nums[idx]
                idx_without_target += 1
        return idx_without_target


if __name__ == '__main__':
    result = Solution().removeElement([3, 2, 2, 3], 3)


