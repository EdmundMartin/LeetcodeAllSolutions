from typing import Optional, List
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Runtime: 72 ms, faster than 81.40% of Python3 online submissions for Find Mode in Binary Search Tree.
# Memory Usage: 18.4 MB, less than 39.09% of Python3 online submissions for Find Mode in Binary Search Tree.
class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        seen = defaultdict(int)
        max_val = 0
        queue = [root]

        while queue:
            node = queue.pop(0)
            if node is None:
                continue
            seen[node.val] += 1
            max_val = max(seen[node.val], max_val)
            queue.append(node.left)
            queue.append(node.right)

        return [k for k, v in seen.items() if v == max_val]