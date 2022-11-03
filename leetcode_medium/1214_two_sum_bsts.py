from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.seen = set()
        self.processed_one = False
        self.has_two_sum = False

    def dfs_other(self, node: TreeNode, target):
        if node is None:
            return
        if self.has_two_sum:
            return
        self.dfs_other(node.left, target)

        other_val = target - node.val
        if self.processed_one and other_val in self.seen:
            self.has_two_sum = True
            return
        if not self.processed_one:
            self.seen.add(node.val)
        self.dfs_other(node.right, target)

    def twoSumBSTs(self, root1: Optional[TreeNode], root2: Optional[TreeNode], target: int) -> bool:
        self.dfs_other(root1, target)
        self.processed_one = True
        self.dfs_other(root2, target)
        return self.has_two_sum
