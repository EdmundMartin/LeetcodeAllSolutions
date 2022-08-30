from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def in_order_traverse(self, root: Optional[TreeNode], low: int, high: int):
        if root is None:
            return
        if root.val > low:
            self.in_order_traverse(root.left, low, high)
        if root.val >= low and root.val <= high:
            self.total += root.val
        if root.val <= high:
            self.in_order_traverse(root.right, low, high)

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.total = 0
        if not root:
            return self.total
        self.in_order_traverse(root, low, high)
        return self.total
