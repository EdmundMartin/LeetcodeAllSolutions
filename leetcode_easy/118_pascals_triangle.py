
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        base = [
            [1],
            [1, 1],
        ]

        if numRows == 1:
            return [base[0]]
        if numRows == 2:
            return base

        for i in range(2, numRows):
            length = len(base[i - 1])
            new = [0] * (length + 1)
            new[0] = 1
            new[-1] = 1

            for idx in range(1, len(new) - 1):
                new[idx] = base[i - 1][idx - 1] + base[i - 1][idx]
            base.append(new)
        return base


if __name__ == '__main__':
    Solution().generate(5)