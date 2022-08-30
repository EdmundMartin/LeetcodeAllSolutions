

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        magazine_count = dict()
        for char in magazine:
            if char not in magazine_count:
                magazine_count[char] = 0
            magazine_count[char] += 1
        for char in ransomNote:
            if char not in magazine_count:
                return False
            if magazine_count[char] - 1 < 0:
                return False
            magazine_count[char] -= 1
        return True
