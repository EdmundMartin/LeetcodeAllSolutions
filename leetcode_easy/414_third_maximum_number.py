from typing import List


class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        number_set = set(nums)
        if len(number_set) < 3:
            return max(nums)
        nums = sorted(list(number_set), reverse=True)
        return nums[2]


if __name__ == '__main__':
    result = Solution().thirdMax([3, 2, 1])
    print(result)

    result = Solution().thirdMax([2, 1])
    print(result)

    result = Solution().thirdMax([2, 2, 3, 1])
    print(result)