from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def backtrack(remain, comb, start):
            if remain == 0:
                results.append(comb[::])
                return
            if remain < 0:
                return

            for idx in range(start, len(candidates)):
                comb.append(candidates[idx])
                backtrack(remain - candidates[idx], comb, idx)
                comb.pop()
        backtrack(target, [], 0)
        return results