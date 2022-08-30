from typing import List


def split_integer(value: int) -> List[int]:
    results = []

    while value >= 10:
        remainder = value % 10
        value = value // 10
        results.append(remainder)
    results.append(value)
    return results[::-1]


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
        res = split_integer(x)
        return res[::-1] == res


if __name__ == '__main__':
    res = split_integer(128)
    print(res)

    res = split_integer(123)
    print(res)

    res = split_integer(12_000)