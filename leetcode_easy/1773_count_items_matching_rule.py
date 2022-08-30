from typing import List


class Solution:
    def countMatches(self, items: List[str], ruleKey: str, ruleValue: str) -> int:
        mapped = {"type": 0, "color": 1, "name": 2}
        idx = mapped[ruleKey]
        found = 0
        for item in items:
            if item[idx] == ruleValue:
                found += 1
        return found
