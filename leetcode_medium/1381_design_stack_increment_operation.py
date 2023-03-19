from typing import List


class CustomStack:

    def __init__(self, maxSize: int):
        self.max_size = maxSize
        self.stack = []

    def push(self, x: int) -> None:
        if len(self.stack) == self.max_size:
            return
        self.stack.append(x)

    def pop(self) -> int:
        if len(self.stack) == 0:
            return -1
        x, self.stack = self.stack[-1], self.stack[:-1]
        return x

    def increment(self, k: int, val: int) -> None:
        if len(self.stack) == 0:
            return
        for i in range(0, min(len(self.stack), k)):
            self.stack[i] += val