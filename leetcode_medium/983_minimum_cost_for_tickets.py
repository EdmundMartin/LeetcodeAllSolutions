from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:

        cache = {}

        def depth_first_search(idx: int):
            if idx == len(days):
                return 0
            if idx in cache:
                return cache[idx]
            cache[idx] = float('inf')
            for day, cost in zip([1, 7, 30], costs):
                j = idx
                while j < len(days) and days[j] < days[idx] + day:
                    j += 1
                cache[idx] = min(cache[idx], cost + depth_first_search(j))
            return cache[idx]

        return depth_first_search(0)


if __name__ == '__main__':
    result = Solution().mincostTickets([1, 4, 6, 7, 8, 20], [2, 7, 15])
    print(result)