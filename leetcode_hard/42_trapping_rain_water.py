from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:

        maxes = [0] * len(height)
        left_max = 0

        for idx, val in enumerate(height):
            maxes[idx] = left_max
            left_max = max(left_max, val)

        right_max = 0
        idx = len(height) - 1
        while idx >= 0:
            current_height = height[idx]
            min_height = min(right_max, maxes[idx])
            if current_height < min_height:
                maxes[idx] = min_height - current_height
            else:
                maxes[idx] = 0
            right_max = max(right_max, current_height)
            idx -= 1

        return sum(maxes)


if __name__ == '__main__':
    test_array = [0, 8, 0, 0, 5, 0, 0, 10, 0, 0, 1, 1, 0, 3]
    result = Solution().trap(test_array)
    print(result)