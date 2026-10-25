class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # given input
        # temperatures array where temperatures[i] represents daily temperature on the i'th day

        # output
        # result where result[i] is the number of days after the i'th day before a warmer temp,erature appears on the future day
        # if thre is no such day set to 0

        # example
        # in tempertaures [30, 38, 30, 36, 35, 40, 28]
        # result[0] = 1 because there's a warmer temp at temperatures[1]
        # result[1] = 4 because there's a warmer tempterature at temperatures[5]
        # result[2] = 1 because there's a warmer temperatuer at temperatures[3]
        # 

        # general approach
        # this uses a monotonic stack in one way
        # is the stack increasing or decreasing? decreasig
        
        # lets say with the first input
        # monotonic stack = 1 (38) -> 3(36) -> 
        # 1. prpocess 30
        # 2. process 38 -> greater than top of stakc -> so keep popping stack, setting result[popped_elem] = counter (which starts at 1) and then increment counter which mkaes result[0] = 1
        # and then stack has 1 (corresponding to 38) added
        # 3. process 30 -> is not greater os it goes onto stack
        # 4. process 36 -> is greater so then pop and set result[2] to be 1 and then add 36
        # 5. process 35 -> not greater os added
        # 6. process 40 -> is greater so then result[4] becomes 5-4 = 1, result[3] becomes 5-3=2, result[1] becomes 5 - 1 = 4
        # wait so then there's no counter its just index of current_to_add - index of popped


        result = []
        for i in range(len(temperatures)):
            result.append(0)
        
        stack = []

        for i in range(len(temperatures)):
            # print(f"stack currently {stack}")
            while len(stack) > 0 and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                result[index] = i - index
            
            stack.append(i)
        
        return result