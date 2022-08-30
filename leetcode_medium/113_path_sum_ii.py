from typing import List, Optional


class TreeNode:
    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.values = []

    def recursive_solution(self, node: TreeNode, path: List[int], target: int):
        if node is None:
            return

        if node.left is None and node.right is None:
            path.append(node.val)
            if sum(path) == target:
                self.values.append(path)
            return
        path.append(node.val)
        self.recursive_solution(node.left, path[:], target)
        self.recursive_solution(node.right, path[:], target)

    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.recursive_solution(root, [], targetSum)
        return self.values
