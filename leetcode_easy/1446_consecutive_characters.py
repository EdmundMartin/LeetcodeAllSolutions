

class Solution:
    def maxPower(self, s: str) -> int:
        longest = -1
        current = 0
        prev = None
        for char in s:
            if char == prev:
                current += 1
            else:
                current = 1
            longest = max(longest, current)
            prev = char
        return longest