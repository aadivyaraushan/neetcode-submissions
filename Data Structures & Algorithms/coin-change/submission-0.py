class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def recurse(remaining):
            # returns fewest num of coins for a given remaining amount
            if remaining == 0:
                # need 0 coins for 0 remaining
                return 0
            if remaining in memo:
                return memo[remaining]

            # lets say i have 12 at start
            # after process
            minim = float('inf')
            for coin in coins:
                if remaining - coin >= 0:
                    minim = min(1 + recurse(remaining - coin), minim)
            memo[remaining] = minim
            return minim

        # in the case hat from the first value coins arent sufficient
        val = recurse(amount)
        if val == float('inf'):
            return -1
        return val