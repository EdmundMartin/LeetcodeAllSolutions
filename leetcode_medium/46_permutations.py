from typing import List


def recursive_generate(prefix: List[int], nums: List[int], values: List[int]) -> None:
    if len(nums) == 0:
        values.append(prefix)
        return
    for idx, num in enumerate(nums):
        copy_nums = nums[:]
        popped = copy_nums.pop(idx)
        new_prefix = prefix[:]
        new_prefix.append(popped)
        recursive_generate(new_prefix, copy_nums, values)


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        values = []
        recursive_generate([], nums, values)
        return values


if __name__ == '__main__':
    test_nums = [1, 2, 3]
    result = Solution().permute(test_nums)
    print(result)