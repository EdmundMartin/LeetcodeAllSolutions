

class Solution:
    def numberOfMatches(self, n: int) -> int:

        matches = 0
        while n > 1:
            if n % 2 != 0:
                matches += (n - 1) // 2
                n = (n // 2) + 1
            else:
                matches += n // 2
                n = n // 2
        return matches


if __name__ == '__main__':
    result = Solution().numberOfMatches(7)
    print(result)

    result = Solution().numberOfMatches(14)
    print(result)