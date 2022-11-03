from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.result = ""

    def depth_first_search(self, node: Optional[TreeNode]):
        if node is None:
            return
        self.result += str(node.val)

        if node.left is None and node.right is None:
            return

        self.result += "("
        self.depth_first_search(node.left)
        self.result += ")"

        if node.right is not None:
            self.result += "("
            self.depth_first_search(node.right)
            self.result += ")"

    def tree2str(self, root: Optional[TreeNode]) -> str:
        self.depth_first_search(root)
        return self.result