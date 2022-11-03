from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.max_sum = float('inf')

    def recursive(self, root: Optional[TreeNode]):
        if root is None:
            return 0

        left_gain = self.recursive(root.left)
        left_gain = max(left_gain, 0)

        right_gain = self.recursive(root.right)
        right_gain = max(right_gain, 0)

        self.max_sum = max(self.max_sum, left_gain + right_gain + root.val)

        return root.val + max(left_gain, right_gain)

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.recursive(root)
        return self.max_sum
