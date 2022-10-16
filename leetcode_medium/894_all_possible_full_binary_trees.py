from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Runtime: 177 ms, faster than 95.45% of Python3 online submissions for All Possible Full Binary Trees.
# Memory Usage: 18.9 MB, less than 37.75% of Python3 online submissions for All Possible Full Binary Trees.
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        dp = {}

        def backtracking(n: int):
            if n == 0:
                return []
            if n == 1:
                return [TreeNode(0)]

            if n in dp:
                return dp[n]
            result = []

            # Go through n - 1 nodes - due to range
            for left in range(n):
                right = n - 1 - left
                left_trees, right_trees = backtracking(left), backtracking(right)

                for tree_one in left_trees:
                    for tree_two in right_trees:
                        result.append(TreeNode(0, tree_one, tree_two))
            dp[n] = result
            return result

        return backtracking(n)