from typing import List


class Node:
    def __init__(self, val: int):
        self.val = val
        self.children = []

    def __repr__(self):
        return "Val: {}, Children:{}".format(self.val, self.children)


class Solution:

    def __init__(self):
        self.to_kill = []

    def recurse(self, node: Node, target: int, should_kill: bool):
        kill_next = False
        if node.val == target or should_kill:
            self.to_kill.append(node.val)
            kill_next = True
        what_do = should_kill or kill_next
        for child in node.children:
            self.recurse(child, target, what_do)

    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        created_nodes = {}
        root = None
        for idx in range(len(pid)):
            parent_num = ppid[idx]
            child_num = pid[idx]

            if parent_num != 0 and parent_num not in created_nodes:
                parent_node = Node(parent_num)
                created_nodes[parent_num] = parent_node
            elif parent_num != 0:
                parent_node = created_nodes[parent_num]

            if child_num not in created_nodes:
                child_node = Node(child_num)
                created_nodes[child_num] = child_node
            else:
                child_node = created_nodes[child_num]

            if parent_num == 0:
                root = child_node
            else:
                parent_node.children.append(child_node)
        self.recurse(root, kill, False)
        return self.to_kill


if __name__ == '__main__':
    Solution().killProcess([1, 3, 10, 5], [3, 0, 5, 3], 5)