class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        def recurse(i, memo={}):
            if i >= len(cost):
                return 0
            if i == len(cost) - 1:
                return cost[-1]
            
            if i in memo:
                return memo[i]

            memo[i] = cost[i] + min(recurse(i+1), recurse(i+2))
            return memo[i]

        return min(recurse(0), recurse(1))