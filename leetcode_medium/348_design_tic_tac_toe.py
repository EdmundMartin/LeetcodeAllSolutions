
class TicTacToe:

    def __init__(self, n: int):
        self.n = n
        self.row = [0] * n
        self.col = [0] * n
        self.diag_one = 0
        self.diag_two = 0
        self.move_counter = 0

    def is_winner(self, row, col, player):
        player_score = player if player == 1 else -1
        self.row[row] += player_score
        self.col[col] += player_score

        if row == col:
            self.diag_one += player_score

        if row + col == self.n - 1:
            self.diag_two += player_score

        if abs(self.row[row]) == self.n or abs(self.col[col]) == self.n or abs(self.diag_one) == self.n or abs(self.diag_two) == self.n:
            return True
        return False

    def move(self, row: int, col: int, player: int) -> int:

        is_winner = self.is_winner(row, col, player)
        if is_winner:
            return player
        return 0


if __name__ == '__main__':
    tic_tac = TicTacToe(3)
    print(tic_tac.board)