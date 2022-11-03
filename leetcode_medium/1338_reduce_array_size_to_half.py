from collections import Counter
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:

        counts = Counter(arr)

        counts = [count for _, count in counts.most_common()]

        total_removed = 0
        set_size = 0
        for count in counts:
            total_removed += count
            set_size += 1
            if total_removed >= len(arr) // 2:
                break
        return set_size