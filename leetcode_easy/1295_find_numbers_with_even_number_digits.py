from typing import List


def count_digits(x: int) -> bool:
    count = 0
    while x >= 10:
        count += 1
        x /= 10
    count += 1
    return count % 2 == 0


# Runtime: 51 ms, faster than 97.78% of Python3 online submissions for Find Numbers with Even Number of Digits.
# Memory Usage: 13.9 MB, less than 85.64% of Python3 online submissions for Find Numbers with Even Number of Digits.
class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        return len(list((filter(count_digits, nums))))


if __name__ == '__main__':
    res = count_digits(12)
    print(res)
    res = count_digits(7)
    print(res)


    res = count_digits(7896)
    print(res)