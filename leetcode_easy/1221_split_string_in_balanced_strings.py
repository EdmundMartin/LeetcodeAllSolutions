

class Solution:
    def balancedStringSplit(self, s: str) -> int:

        counter = 0
        result = 0
        for ch in s:
            if ch == "L":
                counter += 1
            else:
                counter -= 1
            if counter == 0:
                result += 1
        return result