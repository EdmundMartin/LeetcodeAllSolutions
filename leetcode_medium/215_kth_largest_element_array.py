from typing import List
import heapq

def swap_numbers(number: int, k_array: List[int]):
    first_idx = -1
    idx = 0
    while idx < len(k_array) and number > k_array[idx]:
        if idx == 0:
            k_array[idx] = number
            first_idx = 0
            idx += 1
        else:
            k_array[first_idx], k_array[idx] = k_array[idx], k_array[first_idx]
            idx += 1
            first_idx += 1


class SolutionToSlow:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        k_array = [float('-inf')] * k
        for num in nums:
            swap_numbers(num, k_array)
        return k_array[0]


class Solution:
    def findKthLargest(self, nums, k):
        return heapq.nlargest(k, nums)[-1]


if __name__ == '__main__':
    test_nums = [3, 2, 1, 5, 6, 4]
    result = Solution().findKthLargest(test_nums, 2)
    print(result)

    test_nums = [3, 2, 3, 1, 2, 4, 5, 5, 6]
    result = Solution().findKthLargest(test_nums, 4)
    print(result)