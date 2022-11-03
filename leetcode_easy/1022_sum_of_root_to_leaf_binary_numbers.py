from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Runtime: 39 ms, faster than 92.80% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.
# Memory Usage: 14.1 MB, less than 99.20% of Python3 online submissions for Sum of Root To Leaf Binary Numbers.
class Solution:

    def __init__(self):
        self.results = []

    def recursive_solution(self, node: TreeNode, path: str):
        if node is None:
            return

        if node.left is None and node.right is None:
            path += str(node.val)
            self.results.append(int(path, 2))
            return

        path += str(node.val)
        self.recursive_solution(node.left, path)
        self.recursive_solution(node.right, path)

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        self.recursive_solution(root, "")
        return sum(self.results)