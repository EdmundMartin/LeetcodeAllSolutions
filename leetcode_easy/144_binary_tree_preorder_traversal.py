from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def pre_order(self, node: Optional[TreeNode], values: List[int]):
        if node is None:
            return
        values.append(node.val)
        self.pre_order(node.left, values)
        self.pre_order(node.right, values)

    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        self.pre_order(root, values)
        return values