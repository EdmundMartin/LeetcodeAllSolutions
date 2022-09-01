

class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = {'a', 'e', 'i', 'o', 'u'}

        vowel_indexes = []
        s = list(s)
        for idx, ch in enumerate(s):
            if ch.lower() in vowels:
                vowel_indexes.append(idx)
        left = 0
        right = len(vowel_indexes) - 1
        while left < right:
            left_idx = vowel_indexes[left]
            right_idx = vowel_indexes[right]
            s[left_idx], s[right_idx] = s[right_idx], s[left_idx]
            left += 1
            right -= 1
        return "".join(s)
