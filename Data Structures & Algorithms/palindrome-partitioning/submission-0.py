class Solution:
    def partition(self, s: str) -> List[List[str]]:
        # what determines if a string is palindromic?
        # its palindromic if it reads same front and back
        # so we can have 

        # base case:
        # if start == len(s), add palindromes to ans

        # recursive case:
        # for i in range(start, len(s))
        # current_str = s[start:i]
        # if is_palindrome(current_str):
        # palindromes.append(current_str)
        # backtrack(i+1)
        # palindromes.pop(current_str)
        ans = []
        palindromes = []

        def is_palindrome(substr):
            if substr == "":
                return False
            return substr == substr[::-1]

        def backtrack(start):
            nonlocal palindromes
            # print(f"NEW FUNCTION CALL")

            if start == len(s):
                ans.append(palindromes.copy())
                return
            # print(f"start is {start} here")
            for i in range(start, len(s)+1):
                # print(f"i is: {i} while start is {start}")
                substr = s[start:i]
                # print(f"substr selected: {substr}")
                if is_palindrome(substr):
                    # print(f"{substr} is a palindrome")
                    palindromes.append(substr)
                    # print(f"passing in {i} as start")
                    backtrack(i)
                    palindromes.pop()
        
        backtrack(0)
        return ans
