

class MovingAverage:

    def __init__(self, size: int):
        self.window_size = size
        self.values = []

    def next(self, val: int) -> float:
        if len(self.values) == self.window_size:
            self.values = self.values[1:]
            self.values.append(val)
        else:
            self.values.append(val)
        return sum(self.values) / min(len(self.values), self.window_size)


if __name__ == '__main__':
    mv = MovingAverage(3)
    result = mv.next(1)
    print(result)

    result = mv.next(10)
    print(result)

    result = mv.next(3)
    print(result)

    result = mv.next(5)
    print(result)