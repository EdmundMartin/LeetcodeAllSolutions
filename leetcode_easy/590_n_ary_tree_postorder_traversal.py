from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:

    def _traverse(self, node: 'Node', values: List[int]):
        if node.children:
            for child in node.children:
                self._traverse(child, values)
        values.append(node.val)

    def postorder(self, root: 'Node') -> List[int]:
        values = []
        if not root:
            return values
        self._traverse(root, values)
        return values