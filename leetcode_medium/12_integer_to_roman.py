

# Runtime: 52 ms, faster than 92.14% of Python3 online submissions for Integer to Roman.
# Memory Usage: 14 MB, less than 35.57% of Python3 online submissions for Integer to Roman.
class Solution:
    def intToRoman(self, num: int) -> str:
        values = [("M", 1000), ("CM", 900), ("D", 500), ("CD", 400), ("C", 100), ("XC", 90), ("L", 50), ("XL", 40), ("X", 10), ("IX", 9),  ("V", 5), ("IV", 4), ("I", 1)]
        result = ""

        while num > 0:
            idx = 0
            while idx < len(values):
                if values[idx][1] <= num:
                    break
                idx += 1
            values = values[idx:]
            result += values[0][0]
            num -= values[0][1]
        return result


if __name__ == '__main__':
    result = Solution().intToRoman(3)
    print(result)

    result = Solution().intToRoman(58)
    print(result)