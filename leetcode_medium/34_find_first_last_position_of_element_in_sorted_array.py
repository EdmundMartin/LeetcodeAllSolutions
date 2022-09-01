from typing import List


def binary_search(nums: List[int], target: int, search_low: bool):
    left = 0
    right = len(nums) - 1

    found_idx = float('-inf') if search_low is False else float('inf')
    while left <= right:
        middle = (left + right) // 2

        if nums[middle] == target:
            if search_low:
                found_idx = min(found_idx, middle)
                right = middle - 1
            else:
                found_idx = max(found_idx, middle)
                left = middle + 1
        elif nums[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return found_idx if found_idx != float('inf') and found_idx != float('-inf') else -1


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if len(nums) == 0:
            return [-1, -1]
        low = binary_search(nums, target, True)
        if low == -1:
            return [-1, -1]
        high = binary_search(nums, target, False)
        return [low, high]


if __name__ == '__main__':
    test_nums = [5, 7, 7, 8, 8, 10]
    result = Solution().searchRange(test_nums, 8)
    print(result)

    test_nums = [5, 7, 7, 8, 8, 10]
    result = Solution().searchRange(test_nums, 6)
    print(result)