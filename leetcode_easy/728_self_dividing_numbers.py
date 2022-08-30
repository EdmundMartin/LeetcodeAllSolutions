from typing import List


def get_numbers(value: int):
    results = []
    while value >= 10:
        remainder = value % 10
        results.append(remainder)
        value = value // 10
    results.append(value)
    return results


def self_dividing(number: int, nums: List[int]) -> bool:
    for num in nums:
        if num == 0:
            return False
        if number % num != 0:
            return False
    return True


class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        results = []
        while left <= right:
            numbers = get_numbers(left)
            if self_dividing(left, numbers):
                results.append(left)
            left += 1
        return results
