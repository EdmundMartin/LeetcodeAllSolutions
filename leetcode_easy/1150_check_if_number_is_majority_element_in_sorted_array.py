from typing import List


def binary_search_first(nums: List[int], target: int):
    left = 0
    right = len(nums) - 1
    found_element = float('inf')
    while left <= right:
        middle = (left + right) // 2

        if nums[middle] == target:
            found_element = min(found_element, middle)
            right = middle - 1
        elif nums[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return found_element


class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        index = binary_search_first(nums, target)
        if index == float('inf'):
            return False
        count = 0
        while index < len(nums) and nums[index] == target:
            count += 1
            index += 1
        return count / len(nums) > 0.5


if __name__ == '__main__':
    result = Solution().isMajorityElement([10,100,101,101], 101)
    print(result)