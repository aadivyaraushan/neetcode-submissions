from collections import deque

class MinStack:

    def __init__(self):
        self.stack = []
        self.minim_queue = deque()
        # minim_stack is a monotonic queue
        # it's decreasing
        # it stores smallest value at end
        # it stores largest values at start

    def push(self, val: int) -> None:
        self.stack.append(val)
        if len(self.minim_queue) == 0:
            self.minim_queue.append(val)
        else:
            if val <= self.minim_queue[-1]:
                self.minim_queue.append(val)
            else:
                self.minim_queue.appendleft(val)


    def pop(self) -> None:
        if self.stack[-1] == self.minim_queue[-1]:
            self.minim_queue.pop()
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.minim_queue[-1]
        
