from typing import List


class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        counts = {}
        for num in nums:
            if num in counts:
                counts[num] += 1
            else:
                counts[num] = 1
        pairs = 0
        keys_to_delete = 0
        while max(counts.values()) >= 2:
            for key, value in counts.items():
                if value >= 2:
                    if value == 2:
                        keys_to_delete += 1
                    counts[key] -= 2
                    pairs += 1
        return [pairs, len(counts) - keys_to_delete]


if __name__ == '__main__':
    test_nums = [1, 3, 2, 1, 3, 2, 2]
    res = Solution().numberOfPairs(test_nums)
    print(res)