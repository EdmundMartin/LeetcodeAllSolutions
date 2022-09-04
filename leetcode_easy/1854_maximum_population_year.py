from typing import List
from collections import defaultdict


class Solution:
    def maximumPopulation(self, logs: List[List[int]]) -> int:
        counts = defaultdict(int)

        max_count = 0
        earliest_year = float('inf')
        for log in logs:
            for i in range(log[0], log[1]):
                counts[i] += 1
                if counts[i] == max_count:
                    earliest_year = min(i, earliest_year)
                if counts[i] > max_count:
                    max_count = counts[i]
                    earliest_year = i
        return earliest_year




if __name__ == '__main__':
    result = Solution().maximumPopulation([[1993,1999],[2000,2010]])
    print(result)

    result = Solution().maximumPopulation([[1950, 1961],[1960 , 1971],[1970,1981]])
    print(result)