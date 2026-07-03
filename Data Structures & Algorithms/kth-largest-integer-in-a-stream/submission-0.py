import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        nums = [-num for num in nums]
        heapq.heapify(nums)
        self.heap = nums
        self.k = k

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, -val)
        # print(f"after pushing {val}, heap = {self.heap}")
        stack = []
        for i in range(self.k - 1):
            if len(self.heap) == 0:
                break 
            removed = self.heap[0]
            heapq.heappop(self.heap)
            stack.append(removed)
        # print(f"heap after popping k = {self.k} times: {self.heap}")
        output = -self.heap[0]
        while stack:
            heapq.heappush(self.heap, stack.pop())
        return output