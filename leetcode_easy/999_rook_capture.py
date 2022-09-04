from typing import List


def search_board(board, start_cords, dir_x: int, dir_y: int):
    start_x, start_y = start_cords

    while 0 <= start_x < 8 and 0 <= start_y < 8:
        result = board[start_x][start_y]
        if result == 'B':
            return 0
        if result == 'p':
            return 1
        start_x += dir_x
        start_y += dir_y
    return 0


class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        start_pos = None

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'R':
                    start_pos = (i, j)
        result = 0
        for combo in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            result += search_board(board, start_pos, combo[0], combo[1])
        return result


if __name__ == '__main__':
    board_one = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","R",".",".",".","p"],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
    result = Solution().numRookCaptures(board_one)
    print(result)

    board_two = [[".",".",".",".",".",".",".","."],[".","p","p","p","p","p",".","."],[".","p","p","B","p","p",".","."],[".","p","B","R","B","p",".","."],[".","p","p","B","p","p",".","."],[".","p","p","p","p","p",".","."],[".",".",".",".",".",".",".","."],[".",".",".",".",".",".",".","."]]
    result = Solution().numRookCaptures(board_two)
    print(result)

    board_three = [[".",".",".",".",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".","p",".",".",".","."],["p","p",".","R",".","p","B","."],[".",".",".",".",".",".",".","."],[".",".",".","B",".",".",".","."],[".",".",".","p",".",".",".","."],[".",".",".",".",".",".",".","."]]
    result = Solution().numRookCaptures(board_three)
    print(result)