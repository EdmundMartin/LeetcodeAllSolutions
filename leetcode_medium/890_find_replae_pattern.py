from typing import List


def matches(word: str, pattern: str) -> bool:
    word_to_pattern = {}
    pattern_to_word = {}

    for word_char, pattern_char in zip(word, pattern):

        if word_char not in word_to_pattern:
            word_to_pattern[word_char] = pattern_char

        if pattern_char not in pattern_to_word:
            pattern_to_word[pattern_char] = word_char

        if pattern_to_word[pattern_char] != word_char or word_to_pattern[word_char] != pattern_char:
            return False
    return True


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        results = []
        for word in words:
            if matches(word, pattern):
                results.append(word)
        return results


if __name__ == '__main__':
    result = matches("abb", "abc")
    print(result)