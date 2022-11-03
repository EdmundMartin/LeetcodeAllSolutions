from typing import List


class Solution:
    def maxNumberOfApples(self, weight: List[int]) -> int:
        if sum(weight) < 5_000:
            return len(weight)
        weight.sort()
        remaining = 5_000
        count = 0
        while weight and weight[0] <= remaining:
            count += 1
            remaining -= weight[0]
            weight = weight[1:]
        return count
