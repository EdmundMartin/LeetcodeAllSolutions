from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def recursive(self, node: TreeNode, running_total: int, target: int):
        if node is None:
            return

        if self.found is True:
            return

        if node.left is None and node.right is None:
            if running_total + node.val == target:
                self.found = True
                return

        self.recursive(node.left, running_total + node.val, target)
        self.recursive(node.right, running_total + node.val, target)


    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        self.found = False
        self.recursive(root, 0, targetSum)
        return self.found
