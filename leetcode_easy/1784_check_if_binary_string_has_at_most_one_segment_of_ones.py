

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if len(s) <= 2:
            return "1" in s
        seen_10 = False
        seen_01 = False
        idx = 0
        while idx < len(s) - 1:
            slice = s[idx:idx+2]
            if slice == "10":
                seen_10 = True
            if slice == "01":
                seen_01 = True
            if seen_10 and seen_01:
                return False
            idx += 1
        return True


if __name__ == '__main__':
    Solution().checkOnesSegment("101")
