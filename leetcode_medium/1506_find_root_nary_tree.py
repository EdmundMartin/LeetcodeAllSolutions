from typing import List


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    def findRoot(self, tree: List['Node']) -> 'Node':
        node_to_parents = {}

        for node in tree:
            if node not in node_to_parents:
                node_to_parents[node] = list()
            for child in node.children:
                if child in node_to_parents:
                    node_to_parents[child].append(node.val)
                else:
                    node_to_parents[child] = [node.val]
        for key, val in node_to_parents.items():
            if len(val) == 0:
                return key