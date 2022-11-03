from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        idx = 1
        while idx < len(prices):
            if prices[idx] > prices[idx - 1]:
                max_profit += prices[idx] - prices[idx - 1]
            idx += 1
        return max_profit
