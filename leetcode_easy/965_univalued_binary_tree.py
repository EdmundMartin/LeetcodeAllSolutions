from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse(root: Optional[TreeNode]) -> bool:
    if root is None:
        return True

    if root.left and root.left.val != root.val:
        return False
    if root.right and root.right.val != root.val:
        return False
    left_same = traverse(root.left)
    return left_same and traverse(root.right)


class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        return traverse(root)
