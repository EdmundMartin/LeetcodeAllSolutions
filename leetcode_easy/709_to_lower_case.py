

class Solution:
    def toLowerCase(self, s: str) -> str:
        result = ""
        for ch in s:
            if ord(ch) >= 97:
                result += ch
            else:
                result += chr(ord(ch) - 32)
        return result