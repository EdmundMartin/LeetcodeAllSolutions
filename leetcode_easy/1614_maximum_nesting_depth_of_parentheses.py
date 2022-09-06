

class Solution:
    def maxDepth(self, s: str) -> int:
        stack = []

        max_size = 0
        for ch in s:
            if ch == "(":
                stack.append(ch)
            if ch == ")":
                max_size = max(max_size, len(stack))
                stack.pop(-1)
        return max_size