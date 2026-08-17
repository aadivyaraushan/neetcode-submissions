class Solution:
    def checkValidString(self, s: str) -> bool:
        max_open = 0
        min_open = 0

        for char in s:
            if char == '(':
                max_open += 1
                min_open += 1
            if char == ')':
                max_open -= 1
                min_open -= 1
            if char == '*':
                max_open += 1
                min_open -=1
            if max_open < 0:
                return False
            min_open = max(0, min_open)
        
        # print(f"max, min open post loop: {max_open}, {min_open}")
        return min_open == 0