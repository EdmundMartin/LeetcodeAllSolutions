from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        prev = None
        max_sum = -1
        current_sum = None

        for num in nums:
            if prev is None:
                current_sum = num
                max_sum = max(num, max_sum)
            elif prev < num:
                current_sum += num
                max_sum = max(current_sum, max_sum)
            else:
                current_sum = num
                max_sum = max(current_sum, max_sum)
            prev = num
        return max_sum


if __name__ == '__main__':
    t_one = [10, 20, 30, 5, 10, 50]
    result = Solution().maxAscendingSum(t_one)
    print(result)

    t_two = [10, 20, 30, 40, 50]
    result = Solution().maxAscendingSum(t_two)
    print(result)

    t_three = [12, 17, 15, 13, 10, 11, 12]
    result = Solution().maxAscendingSum(t_three)
    print(result)