from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def recursive_solution(root: TreeNode) -> int:
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return 1

    min_depth = float('inf')
    if root.left is not None:
        min_depth = min(recursive_solution(root.left), min_depth)
    if root.right is not None:
        min_depth = min(recursive_solution(root.right), min_depth)

    return min_depth + 1


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return recursive_solution(root)


class SolutionBFS:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        stack = []

        stack.append((root, 1))

        while stack:
            node, depth = stack.pop(0)
            children = [node.left, node.right]
            if not any(children):
                return depth
            for child in children:
                if child:
                    stack.append((child, depth + 1))