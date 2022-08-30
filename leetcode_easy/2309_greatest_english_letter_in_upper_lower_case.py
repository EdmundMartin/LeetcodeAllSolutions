from string import ascii_uppercase, ascii_lowercase
from collections import defaultdict


# Runtime: 39 ms, faster than 92.58% of Python3 online submissions for Greatest English Letter in Upper and Lower Case.
# Memory Usage: 14.1 MB, less than 26.62% of Python3 online submissions for Greatest English Letter in Upper and Lower Case.
class Solution:
    def greatestLetter(self, s: str) -> str:
        res = defaultdict(set)

        upper = set(ascii_uppercase)
        for char in s:
            if char in upper:
                res[char].add("U")
            else:
                res[char.upper()].add("L")
        max_letter = None
        for ch, val in res.items():
            if len(val) == 2:
                if max_letter is None:
                    max_letter = ch.upper()
                else:
                    max_letter = ch.upper() if ascii_uppercase.index(ch) > ascii_uppercase.index(max_letter) else max_letter
        return max_letter if max_letter is not None else ""
