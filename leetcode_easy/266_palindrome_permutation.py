

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        counter = dict()
        for val in s:
            if val not in counter:
                counter[val] = 1
            else:
                counter[val] += 1
        count_odd = 0
        for v in counter.values():
            if v % 2 != 0:
                if count_odd == 1:
                    return False
                count_odd = 1
        return True
