from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.values = []
        self.idx = 0
        self._inorder(root, self.values)

    def _inorder(self, node: Optional[TreeNode], values: List[int]):
        if node is None:
            return
        self._inorder(node.left, values)
        values.append(node.val)
        self._inorder(node.right, values)

    def next(self) -> int:
        val = self.values[self.idx]
        self.idx += 1
        return val

    def hasNext(self) -> bool:
        return self.idx < len(self.values)
