from typing import List


class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        max_val = float('-inf')
        for word in strs:
            if all(i.isdigit() for i in word):
                max_val = max(max_val, int(word))
            else:
                max_val = max(max_val, len(word))
        return max_val
