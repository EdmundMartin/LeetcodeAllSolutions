from typing import List


def lower_bound(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    output = -1
    while left <= right:
        middle = (left + right) // 2
        if nums[middle] == target:
            output = middle
            right = middle - 1
        elif nums[middle] > target:
            right = middle - 1
        else:
            left = middle + 1
    return output


class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        nums = sorted(nums)
        result = []
        left = lower_bound(nums, target)
        if left == -1:
            return result
        while left < len(nums) and nums[left] == target:
            result.append(left)
            left += 1
        return result


if __name__ == '__main__':
    """
    s = Solution().targetIndices([1, 2, 5, 2, 3], 2)
    print(s)
    """

    test_two = [1, 2, 5, 2, 3]
    s = Solution().targetIndices(test_two, 5)