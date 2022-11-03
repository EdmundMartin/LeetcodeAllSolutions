
class Value:
    def __init__(self, value: int, min_val: int):
        self.value = value
        self.min = min_val


class MinStack:

    def __init__(self):
        self.stack = []

    def push(self, val: int) -> None:
        if len(self.stack) == 0:
            min_val = val
        else:
            min_val = min(self.stack[-1].min, val)
        self.stack.append(Value(val, min_val))

    def pop(self) -> None:
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1].value

    def getMin(self) -> int:
        return self.stack[-1].min