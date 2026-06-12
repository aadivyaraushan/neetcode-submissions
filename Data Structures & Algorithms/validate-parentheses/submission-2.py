class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for char in s:
            # if char is one of the opening characters, push onto stack 
            if char == "[" or char == "{" or char == "(":
                stack.append(char)
            else:
                # if char is one of the closing characters, pop top of stack and if top of stack isn't corresponding opening character, return False
                if len(stack) == 0:
                    return False
                else:
                    top = stack.pop()
                if char == "}":
                    if top != "{":
                        return False
                if char == "]":
                    if top != "[":
                        return False
                if char == ")":
                    if top != "(":
                        return False
        
        # return True if we never returned false
        if len(stack) == 0:
            return True
        return False