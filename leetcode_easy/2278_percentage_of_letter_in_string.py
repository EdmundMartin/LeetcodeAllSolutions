
class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count = 0
        for ch in s:
            if ch == letter:
                count += 1
        if count == 0:
            return count
        return int(count / len(s) * 100)


if __name__ == '__main__':
    result = Solution().percentageLetter("foobar", "o")
    print(result)
