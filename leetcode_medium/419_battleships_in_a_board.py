from typing import List


def search_ship(board, x, y, seen):
    board[x][y] = "."
    seen.add((x, y))

    queue = [(x, y)]
    while queue:
        x, y = queue.pop(0)
        for direction in [(1, 0), (-1, 0), (0, 1), (0, -1)]:

            new_x = x + direction[0]
            new_y = y + direction[1]
            if (new_x, new_y) in seen:
                continue
            if new_x >= len(board) or new_x < 0:
                continue
            if new_y >= len(board[0]) or new_y < 0:
                continue
            if (new_x, new_y) in seen:
                continue
            if board[new_x][new_y] == "X":
                board[new_x][new_y] = "."
                queue.append((new_x, new_y))
            seen.add((x, y))
    return


class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        seen = set()
        count = 0
        for r in range(len(board)):
            for c in range(len(board[0])):
                if board[r][c] == "X":
                    search_ship(board, r, c, seen)
                    count += 1
        return count
