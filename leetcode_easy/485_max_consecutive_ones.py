from typing import List


# Runtime: 385 ms, faster than 85.52% of Python3 online submissions for Max Consecutive Ones.
# Memory Usage: 14.3 MB, less than 72.04% of Python3 online submissions for Max Consecutive Ones.
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        longest = 0
        current = 0
        prev = None
        for num in nums:
            if num == 1 and num == prev:
                current += 1
                longest = max(longest, current)
            elif num == 1:
                current = 1
                longest = max(longest, current)
            prev = num
        return longest


if __name__ == '__main__':
    test_one = [1, 1, 0, 1, 1, 1]
    result = Solution().findMaxConsecutiveOnes(test_one)
    print(result)

    test_two = [1, 0, 1, 1, 0, 1]
    result = Solution().findMaxConsecutiveOnes(test_two)
    print(result)