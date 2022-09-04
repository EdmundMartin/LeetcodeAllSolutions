from typing import List
from string import punctuation


def strip_punct(s: str) -> str:
    left = 0
    while left < len(s):
        if s[left] in punctuation:
            left += 1
        else:
            break
    right = len(s) - 1
    while right >= 0:
        if s[right] in punctuation:
            right -= 1
        else:
            break
    return s[left:right+1]


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        banned = set(banned)
        results = dict()
        all_words = []
        for word in paragraph.split(" "):
            if "," in word:
                all_words.extend([w for w in word.split(",") if w != ""])
            else:
                all_words.append(word)

        for word in all_words:
            cleaned = strip_punct(word).lower()
            if cleaned in banned:
                continue
            if cleaned in results:
                results[cleaned] += 1
            else:
                results[cleaned] = 1
        max = (-1, "")
        for k, v in results.items():
            if v > max[0]:
                max = (v, k)
        return max[1]


if __name__ == '__main__':
    res = strip_punct("Bob. hIT, ball")
