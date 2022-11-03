from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def __init__(self):
        self.cousins = {}
        self.x = None
        self.y = None

    def solve(self, node: TreeNode, parent: Optional[TreeNode], depth: int):
        if node is None:
            return node
        if node.val == self.x or node.val == self.y:
            self.cousins[node.val] = (parent, depth)
        self.solve(node.left, node, depth+1)
        self.solve(node.right, node, depth+1)

    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.x = x
        self.y = y
        self.solve(root, None, 0)
        return self.cousins[x][1] == self.cousins[y][1] and self.cousins[x][0] != self.cousins[y][0]
