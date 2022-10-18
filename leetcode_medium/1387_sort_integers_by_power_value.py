from functools import lru_cache


# Runtime: 81 ms, faster than 99.10% of Python3 online submissions for Sort Integers by The Power Value.
# Memory Usage: 14.5 MB, less than 46.13% of Python3 online submissions for Sort Integers by The Power Value.
@lru_cache(maxsize=None)
def collatz_hypothesis(x) -> int:
    if x == 1:
        return 0
    if x % 2 == 0:
        return collatz_hypothesis(x/2) + 1
    else:
        return collatz_hypothesis((3 * x) + 1) + 1


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        return sorted(range(lo, hi + 1), key=collatz_hypothesis)[k-1]


if __name__ == '__main__':
    result = collatz_hypothesis(15)
    print(result)