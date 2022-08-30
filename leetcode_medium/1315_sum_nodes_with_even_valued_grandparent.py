from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Runtime: 103 ms, faster than 98.53% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.
# Memory Usage: 17.6 MB, less than 91.26% of Python3 online submissions for Sum of Nodes with Even-Valued Grandparent.
class Solution:

    def traverse(self, node: Optional[TreeNode], parent: Optional[TreeNode], grandparent: Optional[TreeNode]):
        if node is None:
            return
        if grandparent is not None and grandparent.val % 2 == 0:
            self.total += node.val
        self.traverse(node.left, node, parent)
        self.traverse(node.right, node, parent)

    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.total = 0
        self.traverse(root, None, None)
        return self.total
