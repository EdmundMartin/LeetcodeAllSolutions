

def index_of(word: str, ch: str):
    idx = -1
    for current_idx, w in enumerate(word):
        if w == ch:
            return current_idx
    return idx


def reverse(pref: str) -> str:
    values = list(pref)
    left = 0
    right = len(pref) - 1
    while left < right:
        values[left], values[right] = values[right], values[left]
        left += 1
        right -= 1
    return ''.join(values)


class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        pref_idx = index_of(word, ch)
        if pref_idx == -1:
            return word
        return reverse(word[:pref_idx+1]) + word[pref_idx+1:]


if __name__ == '__main__':
    test_val = "abcdefd"
    result = Solution().reversePrefix(test_val, "d")
    print(result)
    print("dcbaefd")
    assert result == "dcbaefd"