from string import ascii_lowercase


class Solution:
    def minTimeToType(self, word: str) -> int:
        min_typing = len(word)
        chars = list(ascii_lowercase)

        move = abs(chars.index('a') - chars.index(word[0]))
        min_typing += min(move, 26 - move)
        idx = 1
        while idx < len(word):
            move = abs(chars.index(word[idx]) - chars.index(word[idx - 1]))
            min_typing += min(move, 26 - move)
            idx += 1
        return min_typing


if __name__ == '__main__':
    """
    result = Solution().minTimeToType("abc")
    print(result)
    """

    result = Solution().minTimeToType("bza")
    print(result)