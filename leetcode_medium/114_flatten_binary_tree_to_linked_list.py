from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def traverse(pivot: Optional[TreeNode]):
    if pivot is None:
        return

    if pivot.left is None and pivot.right is None:
        return pivot
    left_tail = traverse(pivot.left)

    right_tail = traverse(pivot.right)

    if left_tail is not None:
        left_tail.right = pivot.right
        pivot.right = pivot.left
        pivot.left = None

    return left_tail if right_tail is None else right_tail


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        traverse(root)