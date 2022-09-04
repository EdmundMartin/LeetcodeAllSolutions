from typing import List


class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        copy = [-1] * len(arr)
        idx = len(arr) - 1
        while idx >= 0:
            if idx == len(arr):
                continue
            else:
                if idx + 1 >= len(arr):
                    copy[idx] = -1
                else:
                    copy[idx] = max(arr[idx+1:])
            idx -= 1
        return copy


if __name__ == '__main__':
    test_arr = [17, 18, 5, 4, 6, 1]
    output = Solution().replaceElements(test_arr)
    print(output)