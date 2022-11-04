from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.seen_values = set()
        if self.root:
            self.root.val = 0
            self.seen_values.add(0)
        self.recover_tree(self.root)

    def recover_tree(self, node: TreeNode):
        if node is None:
            return

        if node.left is not None:
            node.left.val = 2 * node.val + 1
            self.seen_values.add(node.left.val)
        if node.right is not None:
            node.right.val = 2 * node.val + 2
            self.seen_values.add(node.right.val)
        self.recover_tree(node.left)
        self.recover_tree(node.right)

    def find(self, target: int) -> bool:
        return target in self.seen_values
