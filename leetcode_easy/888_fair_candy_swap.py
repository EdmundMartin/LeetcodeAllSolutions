from typing import List


class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        diff = (sum(aliceSizes) - sum(bobSizes)) // 2
        a_set = set(aliceSizes)
        for i in set(bobSizes):
            if i + diff in a_set:
                return [diff + i, i]


if __name__ == '__main__':
    res = Solution().fairCandySwap([1, 1], [2, 2])