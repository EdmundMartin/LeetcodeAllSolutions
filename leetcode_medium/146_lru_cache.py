
class Node:
    def __init__(self, key: int, value: int):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, node: Node):
        if self.head is None:
            self.head = node
            self.tail = node
        else:
            head = node
            head.next = self.head
            self.head.prev = head
            self.head = head

    def remove(self, node: Node):
        if node == self.head:
            if node.next is not None:
                self.head = node.next
            else:
                self.head = None
            return

        if node == self.tail:
            if node.prev is not None:
                self.tail = node.prev

        next_node = node.next
        prev_node = node.prev
        if next_node is not None:
            next_node.prev = prev_node
        if prev_node is not None:
            prev_node.next = next_node


class LRUCache:

    def __init__(self, capacity: int):
        self.node_map = {}
        self.capacity = capacity
        self.linked_list = LinkedList()

    def get(self, key: int) -> int:
        if key not in self.node_map:
            return -1
        node = self.node_map[key]
        self.linked_list.remove(node)
        self.linked_list.add(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        if key in self.node_map:
            node = self.node_map[key]
            node.value = value
            self.linked_list.remove(node)
            self.linked_list.add(node)
        else:
            if len(self.node_map) == self.capacity:
                tail = self.linked_list.tail
                self.node_map.pop(tail.key)
                self.linked_list.remove(tail)
            node = Node(key, value)
            self.node_map[key] = node
            self.linked_list.add(node)