from typing import List


class SolutionToSlow:

    def __init__(self):
        self.min_cost = float('inf')

    def recursive(self, costs: List[int], idx, running_cost):
        if idx >= len(costs):
            self.min_cost = min(running_cost, self.min_cost)
            return
        running_cost += costs[idx]
        self.recursive(costs, idx + 1, running_cost)
        self.recursive(costs, idx + 2, running_cost)

    def minCostClimbingStairs(self, cost: List[int]) -> int:
        self.recursive(cost, 0, 0)
        self.recursive(cost, 1, 0)
        return self.min_cost


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        for idx in range(len(cost) - 1, -1, -1):

            if idx + 2 >= len(cost) or idx + 1 >= len(cost):
                continue

            other_cost = min(cost[idx+1], cost[idx+2])
            cost[idx] = other_cost + cost[idx]
        return min(cost[0], cost[1])






if __name__ == '__main__':
    result = Solution().minCostClimbingStairs([10, 15, 20])
    print(result)