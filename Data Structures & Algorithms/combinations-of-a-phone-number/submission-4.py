class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        chars = {
            "1": "",
            "2": "abc",
            "3": "def",
            "4": "ghi", 
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        # some kind of cross product based appraoch would work here
        # what we are looking for is really a cross of multiple sets
        # 1 set = 1 digit's characters
        # and hte logic here is like a nested for loop
        combos = []
        
        def backtrack(combo, start):
            nonlocal combos
            if len(combo) == len(digits) and len(digits) != 0:
                combos.append("".join(combo))
                return
            if start >= len(digits):
                return
            for char in chars[digits[start]]:
                combo.append(char)
                backtrack(combo, start+1)
                combo.pop()
                
        backtrack([], 0)  
        
        return combos