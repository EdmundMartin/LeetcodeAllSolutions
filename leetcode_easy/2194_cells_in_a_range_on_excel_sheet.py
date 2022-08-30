from string import ascii_uppercase
from typing import List


class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        first_idx = ascii_uppercase.index(s[0])
        second_idx = ascii_uppercase.index(s[3])

        chars = ascii_uppercase[first_idx:second_idx+1]
        small, big = int(s[1]), int(s[4])
        results = []
        for char in chars:
            for i in range(small, big + 1):
                results.append(f"{char}{i}")
        return results


if __name__ == '__main__':
    result = Solution().cellsInRange("K1:L2")
    print(result)