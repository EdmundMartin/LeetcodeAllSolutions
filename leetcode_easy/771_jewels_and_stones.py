
class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        all_jewels = set(jewels)
        return sum([1 if s in all_jewels else 0 for s in stones])