

class Solution:
    def judgeCircle(self, moves: str) -> bool:
        start = [0, 0]
        for mov in moves:
            if mov == "U":
                start[0] += 1
            elif mov == "D":
                start[0] -= 1
            elif mov == "L":
                start[1] -= 1
            else:
                start[1] += 1
        return start == [0, 0]


# Runtime: 56 ms, faster than 87.07% of Python3 online submissions for Robot Return to Origin.
# Memory Usage: 14.2 MB, less than 38.43% of Python3 online submissions for Robot Return to Origin.
class SolutionAlt:
    def judgeCircle(self, moves: str) -> bool:
        return moves.count("U") == moves.count("D") and moves.count("L") == moves.count("R")


