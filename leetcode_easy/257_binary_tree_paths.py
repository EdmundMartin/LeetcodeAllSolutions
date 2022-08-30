from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Runtime: 38 ms, faster than 84.40% of Python3 online submissions for Binary Tree Paths.
# Memory Usage: 14 MB, less than 29.10% of Python3 online submissions for Binary Tree Paths.
class Solution:

    def recursive_solve(self, prefix: str, node: Optional[TreeNode], is_leaf: bool):
        if node is None:
            if is_leaf:
                self.results.add(prefix)
            return
        if prefix == "":
            additional = f"{node.val}"
        else:
            additional = f"->{node.val}"
        is_leaf = node.left is None and node.right is None
        self.recursive_solve(prefix + additional, node.left, is_leaf)
        self.recursive_solve(prefix + additional, node.right, is_leaf)

    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        self.results = set()
        self.recursive_solve("", root, root.right is None and root.left is None)
        return list(self.results)
