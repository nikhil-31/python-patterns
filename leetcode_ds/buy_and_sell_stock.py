"""
Best time to buy and sell a stock

You are given an array prices where prices[i] is the price of a given stock on
the ith day.

You want to maximize your profit by choosing a single day to buy one stock and
choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.

Link to leetcode
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Complexity Analysis
Time complexity: O(n). Only a single pass is needed.

Space complexity: O(1). Only two variables are used.
"""

def buy_and_sell_stock(prices: list[int]):
    """
    Buy and sell stock at the maximum profit
    """
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        if price < min_price:
            min_price = price
        elif (price - min_price) > max_profit:
            max_profit = price - min_price

    return max_profit

input_array = [7, 1, 5, 3, 6, 4]

print(buy_and_sell_stock(input_array))
