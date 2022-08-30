from typing import List


class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        smallest_diff = float('inf')
        smallest_num = None
        for num in nums:
            diff = abs(num)
            if diff < smallest_diff:
                smallest_diff = diff
                smallest_num = num
            elif diff == smallest_diff:
                smallest_num = max(num, smallest_num)
        return smallest_num


if __name__ == '__main__':
    result = Solution().findClosestNumber([-4, -2, 1, 4, 8])
    print(result)