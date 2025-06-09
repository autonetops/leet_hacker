# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        min_value = prices[0]

        for price in prices:
            profit = price - min_value
            if price < min_value:
                min_value = price

            if profit > max_profit:
                max_profit = profit

        return max_profit
