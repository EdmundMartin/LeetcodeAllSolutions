from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram_dictionary = {}
        for word in strs:
            sorted_word = str(sorted(word))
            if sorted_word not in anagram_dictionary:
                anagram_dictionary[sorted_word] = []
            anagram_dictionary[sorted_word].append(word)
        return [
            group for group in anagram_dictionary.values()
        ]
