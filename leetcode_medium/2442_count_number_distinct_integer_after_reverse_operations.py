from typing import List


def reverse_int(num: int) -> int:
    result = []
    while num >= 10:
        remainder = num % 10
        num //= 10
        result.append(remainder)
    result.append(num)
    idx = 0
    total = 0
    for val in reversed(result):
        total += val * (10 ** idx)
        idx += 1
    return total


class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        seen = set()
        for num in nums:
            alt = reverse_int(num)
            seen.add(alt)
            seen.add(num)
        return len(seen)


if __name__ == '__main__':
    res = Solution().countDistinctIntegers([1, 13, 10, 12, 31])
    print(res)