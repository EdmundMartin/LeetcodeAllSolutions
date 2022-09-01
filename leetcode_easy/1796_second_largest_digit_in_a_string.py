
class Solution:
    def secondHighest(self, s: str) -> int:
        seen = set()
        for char in s:
            if char.isdigit() and char not in seen:
                seen.add(int(char))
        if len(seen) < 2:
            return -1
        return sorted(list(seen))[-2]