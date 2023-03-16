from typing import List


def swap_number(nums: List[int], first_idx: int, second_idx: int):
    while first_idx >= 0 and nums[first_idx] > nums[second_idx]:
        nums[first_idx], nums[second_idx] = nums[second_idx], nums[first_idx]
        first_idx -= 1
        second_idx -= 1


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        starting_idx = len(nums1) - n
        while len(nums2) > 0:
            current_number = nums2.pop(0)
            nums1[starting_idx] = current_number
            swap_number(nums1, starting_idx - 1, starting_idx)
            starting_idx += 1


if __name__ == '__main__':
    result = [1, 2, 3, 0, 0, 0]

    Solution().merge(result, 3, [2, 5, 6], 3)
    print(result)