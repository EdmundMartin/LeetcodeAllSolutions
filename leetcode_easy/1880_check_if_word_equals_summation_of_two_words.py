from string import ascii_lowercase


def word_to_int(word: str):
    result = 0
    current_mult = 1
    for char in reversed(word):
        result += ascii_lowercase.index(char) * current_mult
        current_mult = current_mult * 10
    return result


class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        return word_to_int(firstWord) + word_to_int(secondWord) == word_to_int(targetWord)


if __name__ == '__main__':
    print(word_to_int("acb"))

    print(word_to_int("cba"))

    print(word_to_int("cdb"))


