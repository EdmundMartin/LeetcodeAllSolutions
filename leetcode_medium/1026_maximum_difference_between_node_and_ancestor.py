from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.max_diff = 0

    def recursive_search(self, node: Optional[TreeNode], min_ancestor, max_ancestor):
        if node is None:
            return
        if min_ancestor is None or max_ancestor is None:
            min_ancestor = node.val
            max_ancestor = node.val
        else:
            if abs(node.val - min_ancestor) > self.max_diff:
                self.max_diff = abs(node.val - min_ancestor)
            if abs(node.val - max_ancestor) > self.max_diff:
                self.max_diff = abs(node.val - max_ancestor)
            min_ancestor = min(node.val, min_ancestor)
            max_ancestor = max(node.val, max_ancestor)
        self.recursive_search(node.left, min_ancestor, max_ancestor)
        self.recursive_search(node.right, min_ancestor, max_ancestor)

    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        self.recursive_search(root, None, None)
        return self.max_diff