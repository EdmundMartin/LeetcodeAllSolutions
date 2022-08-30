from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        levels = []
        if not root:
            return []
        stack = [(root, 0)]

        while stack:
            node, level = stack.pop(0)
            if level == len(levels):
                levels.append([])
            levels[level].append(node.val)
            if node.left:
                stack.append((node.left, level + 1))
            if node.right:
                stack.append((node.right, level + 1))

        return [sum(v) / len(v) for v in levels]