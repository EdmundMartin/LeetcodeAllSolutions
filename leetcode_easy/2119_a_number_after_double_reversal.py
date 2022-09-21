

def reverse_and_strip(x: int):
    result = []
    while x >= 10:
        remainder = x % 10
        result.append(remainder)
        x = x // 10
    result.append(x)

    while len(result) > 0 and result[0] == 0:
        result.pop(0)
    ans = 0
    while result:
        ans += result.pop(0) * (10 ** len(result))
    return ans


class Solution:
    def isSameAfterReversals(self, num: int) -> bool:
        first = reverse_and_strip(num)
        second = reverse_and_strip(first)
        return second == num


if __name__ == '__main__':
    result = Solution().isSameAfterReversals(1800)
    print(result)

    result = Solution().isSameAfterReversals(526)
    print(result)

    result = Solution().isSameAfterReversals(0)
    print(result)
