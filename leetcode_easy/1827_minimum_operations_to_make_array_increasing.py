from typing import List


# Runtime: 135 ms, faster than 94.08% of Python3 online submissions for Minimum Operations to Make the Array Increasing.
# Memory Usage: 14.8 MB, less than 9.48% of Python3 online submissions for Minimum Operations to Make the Array Increasing.
class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ops = 0
        for idx, num in enumerate(nums[1:]):
            if nums[idx] < num:
                continue
            ops += (nums[idx] - num) + 1
            new_num = nums[idx] + 1
            nums[idx + 1] = new_num
        return ops


if __name__ == '__main__':
    result = Solution().minOperations([1, 1, 1])
    print(result)

    result = Solution().minOperations([1, 5, 2, 4, 1])
    print(result)