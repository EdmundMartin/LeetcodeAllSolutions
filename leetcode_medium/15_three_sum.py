from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = set()
        for idx in range(len(nums) - 2):
            left = idx + 1
            right = len(nums) - 1
            while left < right:
                total = nums[idx] + nums[left] + nums[right]
                if total == 0:
                    triplets.add((nums[idx], nums[left], nums[right]))
                    left += 1
                    right -= 1
                elif total > 0:
                    right -= 1
                else:
                    left += 1
        return [list(t) for t in triplets]
