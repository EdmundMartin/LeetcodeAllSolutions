from typing import List


class SolutionBruteForce:

    def __init__(self):
        self.result = 0

    def solve(self, nums: List[int], idx: int, sum: int):
        if idx >= len(nums):
            self.result = max(sum, self.result)
            return
        self.solve(nums, idx + 1, sum + 0)
        self.solve(nums, idx + 2, sum + nums[idx])

    def rob(self, nums: List[int]) -> int:
        self.solve(nums, 0, 0)
        return self.result


class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2


if __name__ == '__main__':
    res = Solution().rob([1, 2, 3, 1])
    print(res)

    res = Solution().rob([2, 7, 9, 3, 1])
    print(res)