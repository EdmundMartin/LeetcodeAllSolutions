from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = None
        self.right = None


class Solution:

    def __init__(self):
        self.prev = 0

    def traverse(self, root: Optional[TreeNode]):
        if root is None:
            return

        self.traverse(root.right)
        self.prev = root.val + self.prev
        root.val = self.prev
        self.traverse(root.left)

    def bstToGst(self, root: TreeNode) -> TreeNode:
        self.traverse(root)
        return root