from typing import List


class Player:
    def __init__(self):
        self.wins = 0
        self.losses = 0


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        undefeated = set()
        losses = dict()

        for match in matches:
            winner, loser = match
            if loser in undefeated:
                undefeated.remove(loser)
            if winner not in losses:
                undefeated.add(winner)
            if loser in losses:
                losses[loser] += 1
            else:
                losses[loser] = 1

        one_loss = [k for k, v in losses.items() if v == 1]

        return [sorted(list(undefeated)), sorted(one_loss)]