

class Solution:
    def capitalizeTitle(self, title: str) -> str:
        words = title.split(" ")

        for idx, word in enumerate(words):
            if len(word) <= 2:
                words[idx] = word.lower()
            else:
                words[idx] = word[:1].upper() + word[1:].lower()
        return ' '.join(words)