import heapq
from typing import List
import math


class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        count = 0
        while count < k:
            heapq._heapify_max(gifts)
            max_pile = heapq._heappop_max(gifts)
            gifts.append(int(math.sqrt(max_pile)))
            count += 1
        return sum(gifts)