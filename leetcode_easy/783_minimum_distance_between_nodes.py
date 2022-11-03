from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.prev = float('-inf')
        self.min_diff = float('inf')

    def dfs(self, node: TreeNode) -> None:
        if node is None:
            return

        self.dfs(node.left)

        self.min_diff = min(self.min_diff, node.val - self.prev)
        self.prev = node.val
        self.dfs(node.right)

    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.min_diff
