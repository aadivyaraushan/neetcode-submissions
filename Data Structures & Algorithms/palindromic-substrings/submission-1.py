class Solution:
    def countSubstrings(self, s: str) -> int:
        memo = []
        for i in range(len(s)):
            row = []
            for j in range(len(s)):
                row.append(-1)
            memo.append(row)
        

        def is_palindrome(l, r):
            if l >= r:
                memo[l][r] = True
                return True
            if s[l] != s[r]:
                memo[l][r] = False
                return False
            if memo[l][r] != -1:
                return memo[l][r]
            
            memo[l][r] = is_palindrome(l+1, r-1)
            return memo[l][r]
        
        num = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                if is_palindrome(i, j):
                    num += 1
        
        return num