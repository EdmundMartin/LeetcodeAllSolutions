from typing import List, Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        level_store = defaultdict(list)
        stack = []
        max_level = 0
        stack.append((root, max_level))

        while stack:
            node, level = stack.pop(0)
            max_level = max(level, max_level)
            level_store[level].append(node.val)

            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))
        flattened = [v for v in level_store.values()]
        return flattened
