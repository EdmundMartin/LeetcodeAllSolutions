from typing import List


def split_number(num: int) -> List[int]:
    result = []
    while num >= 10:
        remainder = num % 10
        num = num // 10
        result.append(remainder)
    result.append(num)
    return result[::-1]


class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        result = []
        for num in nums:
            result.extend(split_number(num))
        return result
