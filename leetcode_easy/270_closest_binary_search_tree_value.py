from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Runtime: 49 ms, faster than 81.78% of Python3 online submissions for Closest Binary Search Tree Value.
# Memory Usage: 16 MB, less than 84.62% of Python3 online submissions for Closest Binary Search Tree Value.
class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = float('inf')
        queue = [root]

        while queue:
            current_node = queue.pop(0)
            if current_node is None:
                continue
            if abs(current_node.val - target) < abs(closest - target):
                closest = current_node.val
            if current_node.val > target:
                queue.append(current_node.left)
            if current_node.val < target:
                queue.append(current_node.right)
            if current_node.val == target:
                return closest
        return closest
