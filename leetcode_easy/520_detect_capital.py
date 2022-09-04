

def count_capitals(s: str) -> int:
    count = 0
    for ch in s:
        if ch == ch.upper():
            count +=1
    return count


class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capital_count = count_capitals(word)
        if capital_count == len(word):
            return True
        if capital_count > 1:
            return False
        if capital_count == 0:
            return True
        return word[0] == word[0].upper()