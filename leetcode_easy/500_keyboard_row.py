from typing import List


class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row_indexes = {}
        for idx, s in enumerate(["qwertyuiop", "asdfghjkl", "zxcvbnm"]):
            for char in s:
                row_indexes[char] = idx
        result = []
        for word in words:
            tmp = word.lower()
            if len(set([row_indexes[v] for v in tmp])) == 1:
                result.append(word)
        return result
