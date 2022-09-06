from typing import List


def combine_nums(nums: List[int]) -> int:
    total = 0
    while len(nums) > 1:
        multiplier = 10 ** (len(nums) - 1)
        total += nums[0] * multiplier
        nums.pop(0)
    total += nums[0]
    return total + 1


def split_nums(n: int) -> List[int]:
    result = []
    while n >= 10:
        remainder = n % 10
        result.append(remainder)
        n = n // 10
    result.append(n)
    result.reverse()
    return result


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        return split_nums(combine_nums(digits))


class SolutionAddition:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)

        for i in range(n):
            idx = n - 1 - i

            if digits[idx] == 9:
                digits[idx] = 0
            else:
                digits[idx] += 1
                return digits
        # Only reachable if all 9s
        digits.insert(0, 1)
        return digits