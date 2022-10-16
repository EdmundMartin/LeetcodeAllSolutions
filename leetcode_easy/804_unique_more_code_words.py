from typing import List
from string import ascii_lowercase


# Runtime: 36 ms, faster than 94.46% of Python3 online submissions for Unique Morse Code Words.
# Memory Usage: 13.9 MB, less than 71.87% of Python3 online submissions for Unique Morse Code Words.
class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        unique_words = set()
        mapping = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]

        for word in words:
            result = ""
            for char in word:
                result += mapping[ascii_lowercase.index(char)]
            unique_words.add(result)
        return len(unique_words)
