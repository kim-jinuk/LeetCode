class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy, sell = 0, 0
        total = 0
        for i in range(1, len(prices)):
            if prices[sell] > prices[i]:
                total += (prices[sell] - prices[buy])
                buy = i
                sell = i
            else:
                sell = i

        if prices[-1] > prices[buy]:
            return total + prices[-1] - prices[buy]

        return total