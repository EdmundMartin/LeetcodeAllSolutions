from typing import List


def binary_search(row, left, right, target):
    if left > right:
        return False
    middle = (left + right) // 2
    if row[middle] == target:
        return True
    elif row[middle] > target:
        return binary_search(row, left, middle-1, target)
    else:
        return binary_search(row, middle+1, right, target)


class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:

        nums = [n for n in mat[0]]

        for num in nums:
            if all([binary_search(r, 0, len(r), num) for r in mat[1:]]):
                return num
        return -1