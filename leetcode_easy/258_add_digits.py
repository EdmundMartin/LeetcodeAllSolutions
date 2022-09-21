

def split_number_sum(num: int) -> int:
    result = []
    while num >= 10:
        remainder = num % 10
        result.append(remainder)
        num = num // 10
    result.append(num)
    return sum(result)


# Runtime: 29 ms, faster than 98.03% of Python3 online submissions for Add Digits.
# Memory Usage: 13.9 MB, less than 9.34% of Python3 online submissions for Add Digits.
class Solution:
    def addDigits(self, num: int) -> int:
        while num > 9:
            num = split_number_sum(num)
        return num


if __name__ == '__main__':
    result = Solution().addDigits(38)
    print(result)

    result = Solution().addDigits(0)
    print(result)