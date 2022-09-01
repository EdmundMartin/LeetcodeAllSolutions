
class Solution:
    def checkString(self, s: str) -> bool:
        seen_b = False
        for char in s:
            if char == 'b' and seen_b is False:
                seen_b = True
            elif char == 'a' and seen_b is True:
                return False
        return True
