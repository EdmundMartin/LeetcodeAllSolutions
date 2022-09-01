

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        counter = {}
        target_set = set(target)
        for ch in s:
            if ch in target_set and ch not in counter:
                counter[ch] = 1
            elif ch in target_set:
                counter[ch] += 1
        count = 0
        while True:
            for ch in target:
                if ch not in counter:
                    return count
                if counter[ch] == 0:
                    return count
                else:
                    counter[ch] -= 1
            count += 1
        return
