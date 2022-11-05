from typing import List


class Solution:
    def luckyNumbers (self, matrix: List[List[int]]) -> List[int]:
        row_mins = [float("inf") for _ in range(len(matrix))]
        col_maxes = [float("-inf") for _ in range(len(matrix[0]))]

        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                value = matrix[row][col]
                row_mins[row] = min(row_mins[row], value)
                col_maxes[col] = max(col_maxes[col], value)

        return list(set(row_mins).intersection(set(col_maxes)))


if __name__ == '__main__':
    res = Solution().luckyNumbers([[3,7,8],[9,11,13],[15,16,17]])
    print(res)