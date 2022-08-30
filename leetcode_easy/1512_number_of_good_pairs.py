from typing import List
from collections import defaultdict


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        unique_combos = set()
        mapping = defaultdict(list)
        for idx, num in enumerate(nums):
            mapping[num].append(idx)
        for idx, num in enumerate(nums):
            others = mapping[num]
            for other in others:
                if other == idx:
                    continue
                elif idx < other:
                    unique_combos.add((idx, other))
        return len(unique_combos)
