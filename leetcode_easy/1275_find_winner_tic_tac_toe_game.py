from typing import List


class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:

        diagonal_one = 0
        diagonal_two = 0
        rows = [0] * 3
        cols = [0] * 3

        for turn, move in enumerate(moves):
            row, col = move
            player = 1 if turn % 2 == 0 else -1
            rows[row] += player
            cols[col] += player
            if row == col:
                diagonal_one += player
            if row + col == 3 - 1:
                diagonal_two += player

            if abs(rows[row]) == 3 or abs(cols[col]) == 3 or abs(diagonal_one) == 3 or abs(diagonal_two) == 3:
                return "A" if turn % 2 == 0 else "B"
        if len(moves) == 9:
            return "Draw"
        return "Pending"


