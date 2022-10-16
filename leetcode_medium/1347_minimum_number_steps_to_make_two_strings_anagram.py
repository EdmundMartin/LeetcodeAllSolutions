

class Solution:
    def minSteps(self, s: str, t: str) -> int:

        dictionary = dict()

        for char in s:
            if char in dictionary:
                dictionary[char] += 1
            else:
                dictionary[char] = 1

        chars_to_change = 0
        for char in t:
            if char in dictionary and dictionary[char] > 0:
                dictionary[char] -= 1
            else:
                chars_to_change += 1
        return chars_to_change
