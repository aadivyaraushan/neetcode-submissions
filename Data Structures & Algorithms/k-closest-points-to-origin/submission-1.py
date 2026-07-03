import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        pairs = []
        for point in points:
            pairs.append((math.sqrt((point[0] * point[0] + point[1] * point[1])), point))
        pairs.sort()
        heapq.heapify(pairs)
        output = []

        for i in range(k):
            _, point = heapq.heappop(pairs)
            output.append(point)
        return output