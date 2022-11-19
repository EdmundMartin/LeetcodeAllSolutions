from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        pairs = []
        while nums:
            biggest = nums.pop(-1)
            small = nums.pop(0)
            pairs.append(small + biggest)
        return max(pairs)


if __name__ == '__main__':
    res = Solution().minPairSum([3, 5, 2, 3])
    print(res)