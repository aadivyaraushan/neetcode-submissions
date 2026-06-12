class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # rules:
        # if we encounter an operator,
        # pop last two
        # apply that operator
        # and push result

        # otherwise just keep pushing numbers onto stack

        stack = []

        for token in tokens:
            if token.lstrip('-').isnumeric():
                stack.append(token)
            else:
                print(f"{token} is not a number")
                print(f"current token: {token}")
                print(f"current stack: {stack}")
                int1 = int(stack.pop())
                int2 = int(stack.pop())
                print(f"int2: {int2}, int1: {int1}")

                if token == '+':
                    stack.append(int2 + int1)
                elif token == '-':
                    stack.append(int2 - int1)
                elif token == '*':
                    stack.append(int2 * int1)
                elif token == '/':
                    stack.append(int2 / int1)
        
        return int(stack.pop())

            