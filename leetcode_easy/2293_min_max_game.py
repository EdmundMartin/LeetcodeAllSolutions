from typing import List


class Solution:
    def minMaxGame(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        while len(nums) >= 2:
            next_nums = []
            idx = 0
            count = 0
            while idx <= len(nums) - 1:
                first, second = nums[idx], nums[idx + 1]
                if count % 2 == 0:
                    next_nums.append(min(first, second))
                else:
                    next_nums.append(max(first, second))
                idx += 2
                count += 1
            nums = next_nums
        return next_nums[0]


if __name__ == '__main__':
    res = Solution().minMaxGame([1, 3, 5, 2, 4, 8, 2, 2])
    print(res)

    res = Solution().minMaxGame([93, 40])
    print(res)