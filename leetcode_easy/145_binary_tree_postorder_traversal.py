from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def post_order(self, node: Optional[TreeNode], values: List[int]):
        if node is None:
            return
        self.post_order(node.left, values)
        self.post_order(node.right, values)
        values.append(node.val)

    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        values = []
        self.post_order(root, values)
        return values
