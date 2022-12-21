from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return
        levels = {}

        queue = [(root, 0)]

        while queue:
            current_node, level = queue.pop(0)
            if not current_node:
                continue

            if level not in levels:
                levels[level] = [current_node]
            else:
                levels[level].append(current_node)
            queue.append((current_node.left, level+1))
            queue.append((current_node.right, level+1))

        for k, nodes in levels.items():
            if k != 0 and k % 2 != 0:
                values = [n.val for n in nodes]
                values.reverse()
                for idx, v in enumerate(values):
                    nodes[idx].val = v
        return root
