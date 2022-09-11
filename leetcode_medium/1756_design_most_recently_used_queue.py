
class MRUQueue:

    def __init__(self, n: int):
        self.stack = [i for i in range(1, n+1)]

    def fetch(self, k: int) -> int:
        val = self.stack[k-1]
        self.stack.pop(k-1)
        self.stack.append(val)
        return val
