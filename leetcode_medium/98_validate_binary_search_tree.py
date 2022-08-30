from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Runtime: 47 ms, faster than 92.39% of Python3 online submissions for Validate Binary Search Tree.
# Memory Usage: 16.5 MB, less than 79.64% of Python3 online submissions for Validate Binary Search Tree.
class Solution:

    def validate(self, node: Optional[TreeNode], min: int, max: int):
        if node is None:
            return True
        if node.val <= min or node.val >= max:
            return False
        valid_left = self.validate(node.left, min, node.val)
        valid_right = self.validate(node.right, node.val, max)
        return valid_left and valid_right

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.validate(root, float('-inf'), float('inf'))