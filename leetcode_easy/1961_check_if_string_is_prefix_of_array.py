from typing import List


class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        prefix = ""
        for word in words:
            prefix += word
            if prefix == s:
                return True
        return False


if __name__ == '__main__':
    s_example = "iloveleetcode"
    s_words = ["i","love","leetcode","apples"]
    result = Solution().isPrefixString(s_example, s_words)
    print(result)