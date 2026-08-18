class Solution:
    def longestPalindrome(self, s: str) -> str:
        memo = []
        for i in range(len(s)):
            row = []
            for j in range(len(s)):
                row.append(-1)
            memo.append(row)
        # print(f"post loop, memo = {memo}")
        

        def is_palindrome(l, r):
            nonlocal memo
            nonlocal s
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
        
        longest = ""
        if len(s) == 1:
            return s

        if is_palindrome(0, len(s) - 1):
            return s

        for i in range(len(s)):
            for j in range(i, len(s)):
                # print(f"consdiering substr {s[i:j+1]}")
                if is_palindrome(i, j) and j-i + 1 > len(longest):
                    longest = s[i:j+1]
        
        return longest
            
