from string import ascii_uppercase


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        mapping = dict()
        for idx, char in enumerate(ascii_uppercase):
            mapping[char] = idx + 1
        sum = 0
        idx = 0
        while idx < len(columnTitle):
            current_char = columnTitle[len(columnTitle) - 1 - idx]
            sum += mapping[current_char] * (26 ** idx)
            idx += 1
        return sum


if __name__ == '__main__':
    Solution().titleToNumber("ZY")
