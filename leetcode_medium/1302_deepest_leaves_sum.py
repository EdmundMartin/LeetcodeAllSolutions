from typing import Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Runtime: 252 ms, faster than 81.82% of Python3 online submissions for Deepest Leaves Sum.
# Memory Usage: 17.8 MB, less than 68.77% of Python3 online submissions for Deepest Leaves Sum.
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        levels = defaultdict(list)
        max_level = 0

        queue = [(root, 0)]
        while queue:
            node, level = queue.pop(0)
            if level > max_level:
                max_level = level
            levels[level].append(node.val)
            if node.left:
                queue.append((node.left, level+1))
            if node.right:
                queue.append((node.right, level+1))
        return sum(levels[max_level])
