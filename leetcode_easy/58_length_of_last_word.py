

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        idx = 0
        last_word = ""
        last_char = None
        while idx < len(s):
            character = s[idx]
            if character != " " and last_char == " ":
                last_word = character
            elif character != " ":
                last_word += character
            last_char = character
            idx += 1
        return len(last_word)


if __name__ == '__main__':
    result = Solution().lengthOfLastWord("Hello World")
    print(result)

    result = Solution().lengthOfLastWord("   fly me   to   the moon  ")
    print(result)

    result = Solution().lengthOfLastWord("luffy is still joyboy")
    print(result)