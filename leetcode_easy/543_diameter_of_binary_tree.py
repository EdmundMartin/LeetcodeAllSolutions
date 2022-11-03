from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Result:
    def __init__(self, height: int, diameter: int):
        self.height = height
        self.diameter = diameter


class Solution:

    def __init__(self):
        self.result = 0

    def recurse(self, node: TreeNode):
        if node is None:
            return -1
        left = self.recurse(node.left)
        right = self.recurse(node.right)

        self.result = max(left + right + 2, self.result)
        return 1 + max(left, right)

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.recurse(root)
        return self.result
