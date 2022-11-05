from typing import List


class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        result = []
        text = text.split(" ")
        for idx, word in enumerate(text):
            if idx > 1 and text[idx - 1] == second and text[idx - 2] == first:
                result.append(word)
        return result
