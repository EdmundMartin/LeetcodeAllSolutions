from typing import List


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for idx in range(0, len(nums), 2):
            freq = nums[idx]
            value = nums[idx + 1]
            result.extend([value] * freq)
        return result


if __name__ == '__main__':
    test_nums = [1, 1, 2, 3]
    result = Solution().decompressRLElist(test_nums)
    print(result)