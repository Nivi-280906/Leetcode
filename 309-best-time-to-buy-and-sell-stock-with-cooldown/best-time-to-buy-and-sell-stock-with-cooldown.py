class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)

        if n == 1:
            return 0

        buy = [0] * n
        sell = [0] * n

        buy[0] = -prices[0]
        sell[0] = 0

        buy[1] = max(buy[0], -prices[1])
        sell[1] = max(sell[0], buy[0] + prices[1])

        for i in range(2, n):
            buy[i] = max(buy[i-1], sell[i-2] - prices[i])
            sell[i] = max(sell[i-1], buy[i-1] + prices[i])

        return sell[n-1]