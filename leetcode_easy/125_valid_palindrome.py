from string import ascii_lowercase, digits


def reverse_string(sent: str):
    chars = list(sent)
    left = 0
    right = len(sent) - 1
    while left < right:
        chars[left], chars[right] = chars[right], chars[left]
        left += 1
        right -= 1
    return ''.join(chars)


def remove_punct(sent: str):
    result = []
    lower_case_letters = set(ascii_lowercase + digits)
    for char in sent:
        lower = char.lower()
        if lower in lower_case_letters:
            result.append(lower)
    return ''.join(result)


class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = remove_punct(s)
        return cleaned == reverse_string(cleaned)


if __name__ == '__main__':
    result = Solution().isPalindrome("race a car")
    print(result)