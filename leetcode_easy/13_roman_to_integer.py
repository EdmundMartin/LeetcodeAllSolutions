

symbol_map = {
    "I": 1,
    "V": 5,
    "X": 10,
    "L": 50,
    "C": 100,
    "D": 500,
    "M": 1000
}


# Runtime: 55 ms, faster than 85.37% of Python3 online submissions for Roman to Integer.
# Memory Usage: 13.9 MB, less than 31.05% of Python3 online submissions for Roman to Integer.
class Solution:
    def romanToInt(self, s: str) -> int:
        idx = len(s) - 1
        sum = 0
        prev = None
        while idx >= 0:
            current = symbol_map[s[idx]]
            if prev and prev > current:
                sum -= current
            else:
                sum += current
                prev = current
            idx -= 1
        return sum


if __name__ == '__main__':
    result = Solution().romanToInt("LVIII")
    print(result)

    result = Solution().romanToInt("MCMXCIV")
    print(result)

    result = Solution().romanToInt("III")
    print(result)