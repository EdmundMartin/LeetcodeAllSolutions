from typing import List


class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def __init__(self):
        self.pre_order_index = 0
        self.idx_map = None
        self.pre_order = None

    def helper(self, in_left_sub_tree: int, in_right_sub_tree: int):

        # No more nodes to place in tree
        if in_left_sub_tree == in_right_sub_tree:
            return None

        root_val = self.pre_order[self.pre_order_index]
        root = TreeNode(root_val)

        idx = self.idx_map[root_val]

        self.pre_order_index += 1
        root.left = self.helper(in_left_sub_tree, idx)
        root.right = self.helper(idx + 1, in_right_sub_tree)
        return root

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:
        in_order_arr = sorted(preorder)
        self.pre_order_index = 0
        self.idx_map = {val: idx for idx, val in enumerate(in_order_arr)}
        self.pre_order = preorder
        return self.helper(0, len(preorder))
