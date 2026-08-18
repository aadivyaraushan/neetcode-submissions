class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def recurse(i):
            if i == len(s):
                return 1
            if i in memo:
                return memo[i]

            c = 0
            if int(s[i]) != 0:
                c += recurse(i+1)
            if 10 <= int(s[i:i+2]) <= 26:
                c += recurse(i+2)
            memo[i] = c
            return c
        
        return recurse(0)