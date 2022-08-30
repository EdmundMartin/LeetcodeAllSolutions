from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def is_mirrored(one: Optional[TreeNode], two: Optional[TreeNode]) -> bool:
    if one is None and two is None:
        return True
    if one is None or two is None:
        return False
    if one.val != two.val:
        return False
    return is_mirrored(one.right, two.left) and is_mirrored(two.right, one.left)


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return is_mirrored(root.left, root.right)