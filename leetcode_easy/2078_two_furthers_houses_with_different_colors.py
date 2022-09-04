from typing import List


class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        n = len(colors)
        i = 0
        j = n - 1

        while colors[j] == colors[0]:
            j -= 1
        while colors[i] == colors[n - 1]:
            i += 1
        return max(j, n - i - 1)


