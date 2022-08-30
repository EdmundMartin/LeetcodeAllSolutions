

class Rod:
    def __init__(self):
        self.colors = [0, 0, 0]

    def add_color(self, color: str):
        if color == 'R':
            self.colors[0] = 1
        elif color == 'G':
            self.colors[1] = 1
        else:
            self.colors[2] = 1


class Solution:
    def countPoints(self, rings: str) -> int:
        rods = [Rod() for _ in range(10)]
        idx = 0
        while idx < len(rings):
            color = rings[idx]
            rod = int(rings[idx + 1])
            rods[rod].add_color(color)
            idx += 2
        return sum([1 if sum(r.colors) == 3 else 0 for r in rods])


if __name__ == '__main__':
    Solution().countPoints("")