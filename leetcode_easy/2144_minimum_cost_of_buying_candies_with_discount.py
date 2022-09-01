from typing import List


class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        candies = sorted(cost)
        cost = 0
        while len(candies) >= 3:
            bought_candies = candies[-3:]
            cost += sum(bought_candies)
            cost -= bought_candies[0]
            candies = candies[:-3]
        if len(candies) > 0:
            cost += sum(candies)
        return cost


class SolutionAlternative:
    def minimumCost(self, cost: List[int]) -> int:
        total_cost = 0
        candy_cost = sorted(cost, reverse=True)
        for idx, candy in enumerate(candy_cost):
            if (idx + 1) % 3 == 0:
                continue
            total_cost += candy
        return total_cost


if __name__ == '__main__':
    candy_array = [6, 5, 7, 9, 2, 2]
    result = SolutionAlternative().minimumCost(candy_array)
    print(result)