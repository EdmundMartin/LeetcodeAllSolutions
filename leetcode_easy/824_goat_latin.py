

# Runtime: 35 ms, faster than 86.69% of Python3 online submissions for Goat Latin.
# Memory Usage: 13.9 MB, less than 16.09% of Python3 online submissions for Goat Latin.
class Solution:
    def toGoatLatin(self, sentence: str) -> str:
        vowels = {"a", "e", "i", "o", "u"}
        words = sentence.split(" ")

        result = []
        for idx, word in enumerate(words):
            if word[0].lower() in vowels:
                new_word = word + "ma" + ("a" * (idx + 1))
                result.append(new_word)
            else:
                new_word = word[1:] + word[:1]
                new_word = new_word + "ma" + ("a" * (idx + 1))
                result.append(new_word)
        return " ".join(result)
