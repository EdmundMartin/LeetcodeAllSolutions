from typing import List


class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        found = True
        while found:
            idx = 0
            on_run = False
            while idx < len(words) - 1:
                if sorted(words[idx]) == sorted(words[idx +1]):
                    words.pop(idx +1)
                    on_run = True
                idx += 1
            if not on_run:
                found = False
        return words
