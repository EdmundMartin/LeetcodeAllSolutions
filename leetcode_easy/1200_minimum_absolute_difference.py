from typing import List
from collections import defaultdict


class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()

        pairs = defaultdict(list)
        for i in range(1, len(arr)):
            diff = abs(arr[i] - arr[i - 1])
            pairs[diff].append([arr[i-1], arr[i]])

        min_diff = min(pairs.keys())
        return pairs[min_diff]


if __name__ == '__main__':
    test_two = [1, 3, 6, 10, 15]
    res = Solution().minimumAbsDifference(test_two)
    print(res)

    test_three = [3,8,-10,23,19,-4,-14,27]
    res = Solution().minimumAbsDifference(test_three)
    print(res)