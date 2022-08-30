

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:

    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:

        queue = [(original, cloned)]

        while queue:
            node_o, node_c = queue.pop(0)

            if node_o is target:
                return node_c

            if node_o.left:
                queue.append((node_o.left, node_c.left))
            if node_o.right:
                queue.append((node_o.right, node_c.right))