

# TODO
class SolutionToSlow:

    def __init__(self):
        self.results = set()

    def recursive_solve(self, current: str, n: int):
        if n == 0:
            self.results.add(current)
            return
        for ch in ['a', 'e', 'i', 'o', 'u']:
            if len(current) == 0 or current[-1] <= ch:
                self.recursive_solve(current+ch, n-1)

    def countVowelStrings(self, n: int) -> int:
        self.recursive_solve("", n)
        return len(self.results)


class Solution:

    def recursive_solve(self, n: int, vowels: int):
        if n == 1:
            return vowels
        if vowels == 1:
            return 1
        return self.recursive_solve(n - 1, vowels) + self.recursive_solve(n, vowels - 1)

    def countVowelStrings(self, n: int) -> int:
        return self.recursive_solve(n, 5)


if __name__ == '__main__':
    res = Solution().countVowelStrings(1)
    print(res)

    res = Solution().countVowelStrings(38)
    print(res)