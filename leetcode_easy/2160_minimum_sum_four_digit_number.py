from typing import List


def split_int(x: int) -> List[int]:
    result = []
    while x >= 10:
        result.append(x % 10)
        x //= 10
    result.append(x)
    return sorted(result, reverse=True)


class Solution:
    def minimumSum(self, num: int) -> int:
        nums = split_int(num)
        return nums[0] + nums[1] + nums[2] * 10 + nums[3] * 10
