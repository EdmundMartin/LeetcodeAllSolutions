from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def traverse_tree(self, node: TreeNode):
        ans = []
        if node is None:
            return []
        if node.left is None and node.right is None:
            ans.append(node.val)
        ans += self.traverse_tree(node.left)
        ans += self.traverse_tree(node.right)
        return ans

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        return self.traverse_tree(root1) == self.traverse_tree(root2)