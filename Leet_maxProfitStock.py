def maxProfitStock(prices, fee):
    n = len(prices)
    buy, sell = [0]*n, [0]*n
    buy[0] = -prices[0]
    for i in range(1, n):
        buy[i] = max(buy[i-1], sell[i-1]-prices[i])
        sell[i] = max(buy[i-1]+prices[i]-fee, sell[i-1])
    return sell[n-1]

prices = [1, 3, 2, 8, 4, 9]
fee =2
maxProfitStock(prices, fee)