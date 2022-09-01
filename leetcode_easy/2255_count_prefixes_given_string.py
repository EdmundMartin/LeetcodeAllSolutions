from typing import List


class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        count = 0
        for word in words:
            if word == s[:len(word)]:
                count += 1
        return count