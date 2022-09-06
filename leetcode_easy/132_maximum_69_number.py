from typing import List


def split_number(n: int) -> List[int]:
    result = []
    while n >= 10:
        remainder = n % 10
        result.append(remainder)
        n = n // 10
    result.append(n)
    result.reverse()
    return result


def combine_number(nums: List[int]):
    total = 0
    while len(nums) > 1:
        multi = 10 ** (len(nums) - 1)
        total += nums[0] * multi
        nums.pop(0)
    total += nums[0]
    return total


# Runtime: 33 ms, faster than 89.67% of Python3 online submissions for Maximum 69 Number.
# Memory Usage: 13.8 MB, less than 54.69% of Python3 online submissions for Maximum 69 Number.
class Solution:
    def maximum69Number (self, num: int) -> int:
        result = split_number(num)
        for idx, num in enumerate(result):
            if num == 6:
                result[idx] = 9
                return combine_number(result)
        return combine_number(result)


if __name__ == '__main__':
    result = split_number(9669)
    print(result)

    result = combine_number(result)
    print(result)