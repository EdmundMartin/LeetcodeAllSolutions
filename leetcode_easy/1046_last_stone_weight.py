from typing import List
import heapq


# Runtime: 36 ms, faster than 89.18% of Python3 online submissions for Last Stone Weight.
# Memory Usage: 13.8 MB, less than 62.78% of Python3 online submissions for Last Stone Weight.
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [s * - 1 for s in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            first = heapq.heappop(stones)
            second = heapq.heappop(stones)
            if first == second:
                continue
            elif first != second:
                new_first = first - second
                heapq.heappush(stones, new_first)
        if len(stones) == 0:
            return 0
        return stones[0] * -1


if __name__ == '__main__':
    res = Solution().lastStoneWeight([2, 7, 4, 1, 8, 1])
    print(res)