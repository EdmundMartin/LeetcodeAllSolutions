

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 0:
            return 0
        current_chars = set()
        longest_str = 1
        current_idx, start_idx = 0, 0
        while current_idx < len(s):
            current_char = s[current_idx]
            if current_char in current_chars:
                longest_str = max(len(current_chars), longest_str)
                current_chars = set()
                current_idx = start_idx + 1
                start_idx = current_idx
            else:
                current_chars.add(current_char)
                current_idx += 1
        return max(len(current_chars), longest_str)


if __name__ == '__main__':
    test_s = "abcabcbb"
    result = Solution().lengthOfLongestSubstring(test_s)