from typing import List


def number_to_array(n: int) -> List[int]:
    results = []
    while n >= 10:
        remainder = n % 10
        n = n // 10
        results.append(remainder)
    results.append(n)
    return results[::-1]


def product(nums: List[int]):
    total = nums[0]
    for num in nums[1:]:
        total *= num
    return total


# Runtime: 37 ms, faster than 80.53% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
# Memory Usage: 13.9 MB, less than 9.81% of Python3 online submissions for Subtract the Product and Sum of Digits of an Integer.
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        split_nums = number_to_array(n)
        return product(split_nums) - sum(split_nums)


if __name__ == '__main__':
    result = Solution().subtractProductAndSum(234)
    print(result)