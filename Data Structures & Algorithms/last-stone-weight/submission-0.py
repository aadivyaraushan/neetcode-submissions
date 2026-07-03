import heapq 

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-stone for stone in stones]
        heapq.heapify(stones)
        while len(stones) > 1:
            x = heapq.heappop(stones)
            y = heapq.heappop(stones)

            if x == y:
                continue
            if x < y:
                heapq.heappush(stones, -y + x)
        if len(stones) == 0:
            return 0
        else:
            return -stones[0]
