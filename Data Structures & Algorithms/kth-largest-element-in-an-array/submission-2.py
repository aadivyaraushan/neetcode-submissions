import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        arr = []
        for num in nums:
            arr.append(-num)
        heapq.heapify(arr)
        for i in range(k-1):
            val = heapq.heappop(arr)

        return arr[0] * -1
