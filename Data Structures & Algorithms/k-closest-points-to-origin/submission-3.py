import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pairs = []
        for point in points:
            dist = ((point[0])**2 + (point[1])**2)**(1/2)
            pairs.append((dist, point))
        heapq.heapify(pairs)
        
        output = []
        for i in range(k):
            _, point = heapq.heappop(pairs)
            output.append(point)
        return output
