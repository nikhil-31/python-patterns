

def buy_and_sell_stocks(nums):
    max_profit = 0.0
    min_price = float("inf")


    for num in nums:
        min_price = min(min_price, num)
        compare_profit = num - min_price
        max_profit = max(max_profit, compare_profit)
    return max_profit 

A = [310, 315, 275, 295, 260, 270, 290, 230, 255, 250]
print(buy_and_sell_stocks(A))