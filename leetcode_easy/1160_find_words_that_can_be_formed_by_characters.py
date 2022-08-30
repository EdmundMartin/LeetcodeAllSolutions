from typing import List


def counter(word: str):
    counter = {}
    for ch in word:
        if ch in counter:
            counter[ch] += 1
        else:
            counter[ch] = 1
    return counter


# Runtime: 166 ms, faster than 80.71% of Python3 online submissions for Find Words That Can Be Formed by Characters.
# Memory Usage: 14.6 MB, less than 36.90% of Python3 online submissions for Find Words That Can Be Formed by Characters.
def check_word(word: str, counter) -> int:
    for ch in word:
        if ch not in counter:
            return 0
        counter[ch] -= 1
        if counter[ch] < 0:
            return 0
    return len(word)


class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        letter_count = counter(chars)
        total = 0
        for word in words:
            total += check_word(word, letter_count.copy())
        return total
