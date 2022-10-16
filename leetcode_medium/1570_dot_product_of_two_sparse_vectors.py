from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.non_zeros = {}
        for idx, num in enumerate(nums):
            if num != 0:
                self.non_zeros[idx] = num

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: 'SparseVector') -> int:
        result = 0

        for key, val in self.non_zeros.items():
            if key in vec.non_zeros:
                result += val * vec.non_zeros[key]
        return result
