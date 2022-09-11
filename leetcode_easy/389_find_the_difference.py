from collections import defaultdict


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        counter = defaultdict(int)
        for ch in s:
            counter[ch] += 1
        for ch in t:
            if counter[ch] - 1 < 0:
                return ch
            counter[ch] -= 1