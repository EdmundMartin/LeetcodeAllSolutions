from typing import List


def meets_conditions(values: List, condition: int) -> bool:
    counts = {}
    for val in values:
        if val in counts and counts[val] + 1 == condition:
            return True
        elif val in counts:
            counts[val] += 1
        else:
            counts[val] = 1
    return False


class Solution:
    def bestHand(self, ranks: List[int], suits: List[str]) -> str:
        if all(s == suits[0] for s in suits):
            return "Flush"
        elif meets_conditions(ranks, 3):
            return "Three of a Kind"
        elif meets_conditions(ranks, 2):
            return "Pair"
        else:
            return "High Card"
