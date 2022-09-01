from string import ascii_lowercase, ascii_uppercase


class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        all_chars = set(ascii_lowercase + ascii_uppercase)
        char_indexes = []
        for idx, char in enumerate(s):
            if char in all_chars:
                char_indexes.append(idx)

        left = 0
        right = len(char_indexes) - 1
        s = list(s)
        while left < right:
            left_idx = char_indexes[left]
            right_idx = char_indexes[right]
            s[left_idx], s[right_idx] = s[right_idx], s[left_idx]
            left += 1
            right -= 1
        return "".join(s)