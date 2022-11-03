from typing import List, Optional
from collections import defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.result = []
        self.seen = defaultdict()

    def depth_first_search(self, node: TreeNode, path):
        if node is None:
            return "#"
        path += ",".join([str(node.val), self.depth_first_search(node.left, path), self.depth_first_search(node.right, path)])

        self.seen[path] += 1

        if self.seen[path] == 2:
            self.result.append(node)
        return path

    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        self.depth_first_search(root, "")
        return self.result