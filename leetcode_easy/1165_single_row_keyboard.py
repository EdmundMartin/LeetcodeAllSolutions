

# Runtime: 58 ms, faster than 80.75% of Python3 online submissions for Single-Row Keyboard.
# Memory Usage: 14.1 MB, less than 11.93% of Python3 online submissions for Single-Row Keyboard.
class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        mapping = {}
        for idx, ch in enumerate(keyboard):
            mapping[ch] = idx
        total = 0
        last_ch = keyboard[0]
        for ch in word:
            delta = mapping[last_ch] - mapping[ch]
            total += abs(delta)
            last_ch = ch
        return total


if __name__ == '__main__':
    test_keyboard_one = "abcdefghijklmnopqrstuvwxyz"
    test_word_one = "cba"

    result = Solution().calculateTime(test_keyboard_one, test_word_one)
    print(result)

    test_keyboard_two = "pqrstuvwxyzabcdefghijklmno"
    test_word_two = "leetcode"

    result = Solution().calculateTime(test_keyboard_two, test_word_two)
    print(result)