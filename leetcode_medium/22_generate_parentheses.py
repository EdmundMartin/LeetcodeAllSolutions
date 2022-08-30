from typing import List


def recursive_generate(prefix: str, opening: int, closing: int, values: List[str]):
    if opening > 0:
        recursive_generate(prefix + "(", opening - 1, closing, values)
    if opening < closing:
        recursive_generate(prefix + ")", opening, closing - 1, values)
    if closing == 0:
        values.append(prefix)


# Runtime: 31 ms, faster than 98.12% of Python3 online submissions for Generate Parentheses.
# Memory Usage: 14.2 MB, less than 40.19% of Python3 online submissions for Generate Parentheses.
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        values = []
        recursive_generate("", n, n, values)
        return values