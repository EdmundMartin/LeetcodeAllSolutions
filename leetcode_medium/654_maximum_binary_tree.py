from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recursive(nums: List[int]):
    if len(nums) == 0:
        return

    max_val = -1
    max_idx = 0
    for idx, num in enumerate(nums):
        if num > max_val:
            max_val = num
            max_idx = idx
    root = TreeNode(nums[max_idx])

    left_copy = nums[::]
    root.left = recursive(left_copy[:max_idx])
    right_copy = nums[::]
    root.right = recursive(right_copy[max_idx+1:])
    return root


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        return recursive(nums)


if __name__ == '__main__':
    result = Solution().constructMaximumBinaryTree([3, 2, 1, 6, 0, 5])
    print(result)
