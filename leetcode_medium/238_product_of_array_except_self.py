from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        length = len(nums)

        left_arr, right_arr = [0] * length, [0] * length

        left_arr[0] = 1
        for idx in range(1, length):

            left_arr[idx] = nums[idx - 1] * left_arr[idx - 1]

        right_arr[-1] = 1
        for idx in reversed(range(length - 1)):
            right_arr[idx] = nums[idx + 1] * right_arr[idx + 1]

        answer = []
        for idx in range(length):
            answer.append(left_arr[idx] * right_arr[idx])

        return answer
