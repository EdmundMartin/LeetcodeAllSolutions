from typing import List


class Solution:
    def maxProfit(self, prices: List[int]):
        max_profit = 0
        min_left = float('inf')

        for price in prices:
            profit = price - min_left
            if profit > max_profit:
                max_profit = profit
            min_left = min(min_left, price)
        return max_profit


if __name__ == '__main__':
    test_prices_one = [7, 1, 5, 3, 6, 4]
    result = Solution().maxProfit(test_prices_one)
    assert result == 5

    test_prices_two = [7, 6, 4, 3, 1]
    result = Solution().maxProfit(test_prices_two)
    assert result == 0