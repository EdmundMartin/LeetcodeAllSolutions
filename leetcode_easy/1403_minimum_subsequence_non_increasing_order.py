from typing import List


class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        total = sum(nums)

        idx = len(nums) - 1
        result = []
        result_sum = 0
        while idx >= 0 and result_sum <= total:
            result.append(nums[idx])
            result_sum += nums[idx]
            total -= nums[idx]
            idx -= 1
        return result


if __name__ == '__main__':
    res = Solution().minSubsequence([4, 4, 10, 9, 8])
    print(res)

    res = Solution().minSubsequence([4, 4, 7, 6, 7])
    print(res)