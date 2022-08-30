from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def in_order(self, node: Optional[TreeNode], values: List[int]):
        if node is None:
            return
        self.in_order(node.left, values)
        values.append(node.val)
        self.in_order(node.right, values)

    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        self.in_order(root, values)
        return values