

class Solution:
    def removeDigit(self, number: str, digit: str) -> str:
        idx = len(number) - 1
        variant = float('-inf')
        while idx >= 0:
            if number[idx] == digit:
                result = number[:idx] + number[idx + 1:]
                if int(result) > variant:
                    variant = int(result)
            idx -= 1
        return str(variant)


if __name__ == '__main__':
    result = Solution().removeDigit("123", "3")
    print(result)

    result = Solution().removeDigit("1231", "1")
    print(result)

    result = Solution().removeDigit("551", "5")
    print(result)