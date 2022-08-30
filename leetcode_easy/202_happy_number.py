from typing import List


def get_numbers(value: int):
    results = []
    while value >= 10:
        remainder = value % 10
        results.append(remainder)
        value = value // 10
    results.append(value)
    return results


def get_next(value: int):
    digits = get_numbers(value)
    total = 0
    for dig in digits:
        total += dig ** 2
    return total


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            n = get_next(n)
        return n == 1



if __name__ == '__main__':
    result = get_numbers(100)
    print(result)