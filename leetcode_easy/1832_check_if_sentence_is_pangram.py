from string import ascii_lowercase


class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        english_letters = set(ascii_lowercase)
        for char in sentence:
            if char in english_letters:
                english_letters.remove(char)
        return len(english_letters) == 0