from typing import List


class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        return max([sum(i) for i in accounts])


if __name__ == '__main__':
    test_one = [[1, 2, 3], [3, 2, 1]]
    result = Solution().maximumWealth(test_one)
    print(result)