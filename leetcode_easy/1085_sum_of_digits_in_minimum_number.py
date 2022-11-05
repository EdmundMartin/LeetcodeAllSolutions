from typing import List


# Runtime: 44 ms, faster than 83.04% of Python3 online submissions for Sum of Digits in the Minimum Number.
# Memory Usage: 13.9 MB, less than 50.88% of Python3 online submissions for Sum of Digits in the Minimum Number.
def check_condition(num: int):
    result = []

    while num >= 10:
        remainder = num % 10
        num //= 10
        result.append(remainder)
    result.append(num)
    return 0 if sum(result) % 2 != 0 else 1


class Solution:
    def sumOfDigits(self, nums: List[int]) -> int:
        nums.sort()
        return check_condition(nums[0])


if __name__ == '__main__':
    result = Solution().sumOfDigits([34,23,1,24,75,33,54,8])
    print(result)

    result = Solution().sumOfDigits([99,77,33,66,55])
    print(result)