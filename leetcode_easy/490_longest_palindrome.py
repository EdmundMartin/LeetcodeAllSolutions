from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = Counter(s)
        answer = 0
        for value in counter.values():
            answer += value // 2 * 2
            if answer % 2 == 0 and value % 2 == 1:
                answer += 1
        return answer
