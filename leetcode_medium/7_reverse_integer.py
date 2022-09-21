

def reverse_int(x: int):
    negative = False
    if x < 0:
        negative = True
    x = abs(x)
    digits = []
    while x >= 10:
        remainder = x % 10
        digits.append(remainder)
        x = x // 10
    digits.append(x)
    result = 0
    while digits:
        first = digits.pop(0)
        result += first * (10 ** len(digits))
    return -result if negative else result


class Solution:
    def reverse(self, x: int) -> int:
        if abs(x) > (2**31) - 1:
            return 0
        ans = reverse_int(x)
        if abs(ans) > (2**31) - 1:
            return 0
        return ans


if __name__ == '__main__':
    Solution().reverse(1534236469)