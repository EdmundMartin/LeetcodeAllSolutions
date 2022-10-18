from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        idx = 1
        max_mountain = None
        max_idx = None
        while idx < len(arr) - 1:
            if arr[idx] > arr[idx - 1] and arr[idx] > arr[idx + 1]:
                if max_mountain and arr[idx] > max_mountain:
                    max_mountain = arr[idx]
                    max_idx = idx
                else:
                    max_mountain = arr[idx]
                    max_idx = idx
            idx += 1
        return max_idx