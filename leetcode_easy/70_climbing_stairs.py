from typing import Dict

class Solution:

    def recursive_solution(self, steps: int, memo: Dict[int, int]):
        if steps in memo:
            return memo[steps]

        number_of_ways = 0
        for i in [1, 2]:
            if i <= steps:
                number_of_ways += self.recursive_solution(steps - i, memo)
        memo[steps] = number_of_ways
        return number_of_ways


    def climbStairs(self, n: int) -> int:
        return self.recursive_solution(n, {1: 1, 2: 2})