from typing import List
from collections import defaultdict
import heapq


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:

        results = defaultdict(int)
        for word in words:
            results[word] += 1
        return heapq.nsmallest(k, results.keys(), key=lambda x: (-results[x], x))


if __name__ == '__main__':
    Solution().topKFrequent(["i","love","leetcode","i","love","coding"], 2)
