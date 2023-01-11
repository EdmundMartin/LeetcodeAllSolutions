from typing import List


class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        for idx, word in enumerate(words):
            next_idx = idx + 1
            while next_idx < len(words):
                if set(word) == set(words[next_idx]):
                    count += 1
                next_idx += 1
        return count
