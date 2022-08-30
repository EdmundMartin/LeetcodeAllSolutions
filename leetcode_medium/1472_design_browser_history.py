
class Node:
    def __init__(self, value: str):
        self.value = value
        self.prev = None
        self.next = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        self.current_pointer = None

    def add(self, node: Node):
        if self.head is None:
            self.head = node
            self.tail = node
            self.current_pointer = node
            return
        node.prev = self.current_pointer
        self.current_pointer.next = node
        self.current_pointer = node

    def back(self, steps: int) -> str:
        count = 0
        current = self.current_pointer
        while count < steps and current.prev:
            current = current.prev
            count += 1
        self.current_pointer = current
        return current.value

    def forward(self, steps: int):
        count = 0
        current = self.current_pointer
        while count < steps and current.next:
            current = current.next
            count += 1
        self.current_pointer = current
        return current.value

    def display(self):
        current = self.head
        results = []
        while current:
            results.append(current.value)
            current = current.next
        return results, self.current_pointer.value


class BrowserHistory:

    def __init__(self, homepage: str):
        self.linked_list = DoublyLinkedList()
        self.linked_list.add(Node(homepage))

    def visit(self, url: str) -> None:
        self.linked_list.add(Node(url))

    def back(self, steps: int) -> str:
        return self.linked_list.back(steps)

    def forward(self, steps: int) -> str:
        return self.linked_list.forward(steps)
