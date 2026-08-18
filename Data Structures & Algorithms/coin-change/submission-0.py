class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [amount + 1] * (amount + 1)

        dp[0] = 0

        # working
        # for 12
        # we go from 12 - 10 = 2 -> 2 - 1 = 1 -> 1 - 1 = 0 takes 3 turns
        # so variable tracked is the amt 


        for a in range(1, amount+1):
            for coin in coins:
                if a - coin >= 0:
                    dp[a] = min(dp[a], 1 + dp[a-coin])
        
        return dp[amount] if dp[amount] != amount + 1 else -1