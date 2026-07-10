class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def backtrack(span, open_used, close_used):
            nonlocal ans
            # base case: if open used == n, return
            if open_used == n and close_used == n:
                ans.append(span)
                return 
            
            # recursive case:
            # if open_used < n: add ( and call recursively
            if open_used < n:
                # print(f"in this function call open_used < n")
                backtrack(span + "(", open_used + 1, close_used)
            # print(f"continues onwards with OU = {open_used} and CU = {close_used}")
            # if open_used > close_used: add ) and call recursively
            if open_used > close_used:
                backtrack(span + ")", open_used, close_used + 1)
                close_used += 1 
        
        backtrack("", 0, 0)
        return ans
