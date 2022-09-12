

class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        output = ""
        count = 0

        for ch in s:
            if ch == "(":
                count += 1
                if count > 1:
                    output += ch
            else:
                count -= 1
                if count > 0:
                    output += ch
        return output