from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def in_order_traversal(self, node: Optional[TreeNode], values: List[int]):
        if node is None:
            return
        self.in_order_traversal(node.left, values)
        if (node.left is None and node.right) or (node.right is None and node.left):
            if node.left is None:
                values.append(node.right.val)
            if node.right is None:
                values.append(node.left.val)
        self.in_order_traversal(node.right, values)

    def getLonelyNodes(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        self.in_order_traversal(root, values)
        return values