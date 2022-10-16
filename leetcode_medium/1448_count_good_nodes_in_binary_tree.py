

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.count = 0

    def recursive(self, node: TreeNode, max_parent: int):
        if node is None:
            return

        if max_parent <= node.val:
            self.count += 1
        max_parent = max(max_parent, node.val)

        self.recursive(node.left, max_parent)
        self.recursive(node.right, max_parent)

    def goodNodes(self, root: TreeNode) -> int:
        self.recursive(root, float('-inf'))
        return self.count