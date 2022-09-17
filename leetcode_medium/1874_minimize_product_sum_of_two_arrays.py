from typing import List


class Solution:
    def minProductSum(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort(reverse=True)

        ans = 0
        for one, two in zip(nums1, nums2):
            ans += one * two
        return ans


if __name__ == '__main__':
    res = Solution().minProductSum([5, 3, 4, 2], [4, 2, 2, 5])
    print(res)

    res = Solution().minProductSum([2, 1, 4, 5, 7], [3, 2, 4, 8, 6])
    print(res)