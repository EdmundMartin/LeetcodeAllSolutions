from typing import List

from collections import defaultdict


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:

        word_set = set(wordDict)

        memo = defaultdict(list)

        def _wordbreak_topdown(s: str):

            if len(s) == 0:
                return [[]]

            if s in memo:
                return memo[s]

            for end_index in range(1, len(s) + 1):
                word = s[:end_index]
                if word in word_set:
                    for sub_sentence in _wordbreak_topdown(s[end_index:]):
                        memo[s].append([word] + sub_sentence)
            return memo[s]

        _wordbreak_topdown(s)

        return [" ".join(words) for words in memo[s]]