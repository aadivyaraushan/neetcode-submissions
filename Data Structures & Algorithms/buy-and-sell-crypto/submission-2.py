class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 1:
            return 0
        left = 0
        max_profit = float('-inf')
        for right in range(len(prices)):
            profit = prices[right] - prices[left]
            if profit > max_profit:
                max_profit = profit
            if profit < 0:
                # this means selling price was lower than buying price
                # so that should be new buying price
                left = right

        return max_profit
