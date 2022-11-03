from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.parent_mapping = {}
        self.root_none = False

    def parent_recurse(self, parent: TreeNode, target: int):
        while parent and parent.val == target:
            if parent.left is not None or parent.right is not None:
                return
            grandpa = self.parent_mapping.get(parent, None)
            if grandpa is None:
                self.root_none = True
                return
            if grandpa.left == parent:
                grandpa.left = None
            else:
                grandpa.right = None
            parent = grandpa

    def solve_problem(self, node: Optional[TreeNode], parent: Optional[TreeNode], target: int):
        if node is None:
            return

        if node.val == target:
            if parent is None and node.left is None and node.right is None:
                return
            if node.left is None and node.right is None:
                if parent.right == node:
                    parent.right = None
                else:
                    parent.left = None
                self.parent_recurse(parent, target)
        if parent:
            self.parent_mapping[node] = parent
        self.solve_problem(node.left, node, target)
        self.solve_problem(node.right, node, target)

    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        self.solve_problem(root, None, target)
        return root if self.root_none is False else None