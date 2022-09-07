from typing import List


def reverse_word(s: str) -> str:
    s = list(s)
    left = 0
    right = len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1
    return ''.join(s)


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if reverse_word(word) == word:
                return word
        return ""