

def reverse(s: str) -> str:
    chars = list(s)
    left = 0
    right = len(s) - 1

    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return ''.join(chars)


class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(' ')

        for idx, w in enumerate(words):
            words[idx] = reverse(w)
        return ' '.join(words)