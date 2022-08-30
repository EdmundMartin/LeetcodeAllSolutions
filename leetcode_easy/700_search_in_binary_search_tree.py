from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Runtime: 96 ms, faster than 74.80% of Python3 online submissions for Search in a Binary Search Tree.
# Memory Usage: 16.5 MB, less than 69.50% of Python3 online submissions for Search in a Binary Search Tree.
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        current_node = root
        while current_node:
            if current_node.val < val:
                current_node = current_node.right
            elif current_node.val > val:
                current_node = current_node.left
            else:
                return current_node
        return None
