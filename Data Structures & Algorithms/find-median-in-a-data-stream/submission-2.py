import heapq

class MedianFinder:

    def __init__(self):
        self.arr = []
        self.n = 0

    def addNum(self, num: int) -> None:
        # print(f"addNum({num}) called")
        l = 0
        r = self.n

        while l < r:
            m = (l + r) // 2 
            # print(f"at iteration start: l = {l} and r = {r}")
            # print(f"iterating with m = {m} and arr[m] = {self.arr[m]}")

            if self.arr[m] >= num:
                r = m
            else:
                l = l + 1
        m = (l + r) // 2 
        # print(f"before calling insertion, m = {m}")
        self.arr.insert(m, num)
        self.n += 1
        # print(f"at the end of this addNum call, arr = {self.arr}")
        

    def findMedian(self) -> float:
        mid = self.n //2

        if self.n % 2 == 0:
            # n is even so find mid elem, mid - 1 elem. mid = n/2 btw.
            # and take average
            # and thats median
            num1 = self.arr[mid-1]
            num2 = self.arr[mid]
            return (num1 + num2) / 2
            
        else:
            # n is odd so find mid/2 elem and thats median
            return self.arr[mid]
        