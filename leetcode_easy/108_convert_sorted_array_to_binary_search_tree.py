from typing import List, Optional

class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.val = value
        self.left = left
        self.right = right


def recursive_build(nums: List[int], left: int, right: int):
    if left > right:
        return

    middle = (left + right) // 2

    root = TreeNode(nums[middle])

    root.left = recursive_build(nums, left, middle - 1)
    root.right = recursive_build(nums, middle + 1, right)
    return root


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return
        return recursive_build(nums, 0, len(nums)-1)