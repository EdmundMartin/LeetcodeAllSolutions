from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        sorted_nums = sorted(nums)

        result_dict = {}
        for idx, num in enumerate(sorted_nums):
            if num in result_dict:
                continue
            result_dict[num] = idx
        results = []
        for num in nums:
            results.append(result_dict[num])
        return results


if __name__ == '__main__':
    test_one = [8, 1, 2, 2, 3]
    s = Solution().smallerNumbersThanCurrent(test_one)
    print(s)
