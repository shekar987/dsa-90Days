"""Day 08: DSA practice workspace."""


from typing import List


QUESTION = """
121. Best Time to Buy and Sell Stock

You are given an array prices where prices[i] is the price of a given stock
on the ith day.

Choose one day to buy one stock and a different future day to sell it.
Return the maximum profit possible. If no profit is possible, return 0.

Examples:
Input: prices = [7,1,5,3,6,4]
Output: 5

Input: prices = [7,6,4,3,1]
Output: 0

Constraints:
1 <= prices.length <= 10^5
0 <= prices[i] <= 10^4
"""


class Solution:
    """Best Time to Buy and Sell Stock solution."""

    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        max_profit = 0

        for price in prices:
            # Buy at the cheapest price seen before or on this day.
            lowest_price = min(lowest_price, price)

            # Sell today and check whether it gives a better profit.
            current_profit = price - lowest_price
            max_profit = max(max_profit, current_profit)

        return max_profit


if __name__ == "__main__":
    solution = Solution()
    checks = [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
    ]

    for prices, expected in checks:
        assert solution.maxProfit(prices) == expected

    print("All Day 08 checks passed.")
