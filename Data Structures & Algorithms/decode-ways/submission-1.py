class Solution:
    def numDecodings(self, s: str) -> int:
        memo = {}

        def recurse(i):
            # returns the # of possible decodings from string s

            if i == len(s):
                return 1
            if s[i] == '0':
                return 0
            if i in memo:
                return memo[i]

            # at any level
            # choice 1: consume one digit
            c = 0
            if int(s[i]) != 0:
                c += recurse(i+1)
            if 10 <= int(s[i:i+2]) <= 26:
                c += recurse(i+2)

            # choice 2: consume two digits
            # here, consumption = moving starting index forward
            memo[i] = c
            print(f"settling on {c} for recurse({i})")
            return c

        
        return recurse(0)