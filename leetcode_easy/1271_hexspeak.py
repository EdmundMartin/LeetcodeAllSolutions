

class Solution:
    def toHexspeak(self, num: str) -> str:
        start = str(hex(int(num)))
        result = ""
        for ch in start[2:]:
            if ch in {"a", "b", "c", "d", "e", "f", "i", "o"}:
                result += ch.upper()
            elif ch.isdigit() and ch in {"1", "0"}:
                if ch == "1":
                    result += "I"
                else:
                    result += "O"
            else:
                return "ERROR"
        return result