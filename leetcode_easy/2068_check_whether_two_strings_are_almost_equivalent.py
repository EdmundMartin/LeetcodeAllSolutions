from collections import defaultdict


def dict_from_word(word: str):
    result = defaultdict(int)
    for ch in word:
        result[ch] += 1
    return result


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        default_one = dict_from_word(word1)
        default_two = dict_from_word(word2)

        all_chars = set(word1 + word2)
        for char in all_chars:
            if abs(default_one[char] - default_two[char]) > 3:
                return False
        return True
