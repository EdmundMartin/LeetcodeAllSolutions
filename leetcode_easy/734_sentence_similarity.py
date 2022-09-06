from typing import List
from collections import defaultdict


class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:

        if len(sentence1) != len(sentence2):
            return False

        close_words = defaultdict(set)
        for word_pairing in similarPairs:
            close_words[word_pairing[0]].add(word_pairing[1])
            close_words[word_pairing[1]].add(word_pairing[0])

        idx = 0
        while idx < len(sentence1):
            if sentence1[idx] == sentence2[idx]:
                idx += 1
            else:
                similar = close_words[sentence1[idx]]
                if sentence2[idx] in similar:
                    idx += 1
                else:
                    return False
        return True