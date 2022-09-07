from typing import List


class Solution:
    def generatePossibleNextMoves(self, currentState: str) -> List[str]:

        output = []

        for idx, val in enumerate(currentState):
            if idx == 0:
                continue
            elif val == "+" and currentState[idx - 1] == "+":
                output.append(
                    currentState[:idx] + "--" + currentState[idx + 2:]
                )
        return output