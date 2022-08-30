from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed = set(allowed)
        count = 0
        for word in words:
            if all(ch in allowed for ch in word):
                count += 1
        return count


if __name__ == '__main__':
    result = Solution().countConsistentStrings("abc", ["a","b","c","ab","ac","bc","abc"])