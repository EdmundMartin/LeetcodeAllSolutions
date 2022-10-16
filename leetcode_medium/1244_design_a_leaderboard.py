from collections import defaultdict
import heapq


class Leaderboard:

    def __init__(self):
        self.scores = defaultdict(int)

    def addScore(self, playerId: int, score: int) -> None:
        self.scores[playerId] += score

    def top(self, K: int) -> int:
        heap = list(self.scores.values())
        heapq.heapify(heap)
        return sum([n for n in heapq.nlargest(K, heap)])

    def reset(self, playerId: int) -> None:
        self.scores[playerId] = 0


if __name__ == '__main__':
    leaderboard = Leaderboard()
    leaderboard.addScore(1, 10)
    leaderboard.addScore(2, 12)
    leaderboard.addScore(3, 5)
    print(leaderboard.top(2))

    leaderboard.reset(1)
    print(leaderboard.top(2))