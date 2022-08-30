from typing import List


class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        idx_less_than_k = -1
        i = len(nums) - 1
        while i >= 0:
            if nums[i] < k:
                idx_less_than_k = i
                break
            i -= 1
        if idx_less_than_k == -1:
            return idx_less_than_k

        closest_sum = None
        while idx_less_than_k > 0:
            left = 0
            right = idx_less_than_k - 1
            while left <= right:

                middle = (left + right) // 2
                current_sum = nums[middle] + nums[idx_less_than_k]
                if current_sum < k:
                    if closest_sum is None:
                        closest_sum = current_sum
                    else:
                        closest_sum = current_sum if current_sum > closest_sum else closest_sum

                if current_sum < k:
                    left += 1
                else:
                    right -= 1
            idx_less_than_k -= 1
        return closest_sum if closest_sum is not None else -1


if __name__ == '__main__':
    test_nums = [34, 23, 1, 24, 75, 33, 54, 8]
    target = 60

    result = Solution().twoSumLessThanK(test_nums, target)
    print(result)

    test_nums = [10, 20, 30]
    result = Solution().twoSumLessThanK(test_nums, 15)
    print(result)