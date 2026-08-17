class Solution:
    def climbStairs(self, n: int) -> int:
        def num_ways(n, memo={}):
            if n in memo:
                return memo[n]

            if n == 1:
                return 1
            if n == 2:
                return 2
            
            memo[n] = num_ways(n-1) + num_ways(n-2)
            return memo[n]
        
        return num_ways(n)