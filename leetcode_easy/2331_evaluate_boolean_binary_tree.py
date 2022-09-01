from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recursive(root: TreeNode):
    if root.val == 0:
        return False
    if root.val == 1:
        return True

    if root.val == 2:
        return recursive(root.left) or recursive(root.right)
    if root.val == 3:
        return recursive(root.left) and recursive(root.right)


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        return recursive(root)