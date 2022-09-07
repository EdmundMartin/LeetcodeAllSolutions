from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def in_order_traversal(root: TreeNode, values):
    if root is None:
        return
    in_order_traversal(root.left, values)
    values.append(root.val)
    in_order_traversal(root.right, values)


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        values = []
        in_order_traversal(root, values)
        return min([values[x+ 1] - values[x] for x in range(len(values) - 1)])