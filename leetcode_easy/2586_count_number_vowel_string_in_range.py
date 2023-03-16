from typing import List


class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        vowels = {"a", "e", "i", "o", "u"}
        words = words[left:right+1]
        print(words)
        count = 0
        for w in words:
            if w[0] in vowels and w[-1] in vowels:
                count += 1
        return count


if __name__ == '__main__':
    res = Solution().vowelStrings(["are", "amy", "u"], 0, 2)
    print(res)
