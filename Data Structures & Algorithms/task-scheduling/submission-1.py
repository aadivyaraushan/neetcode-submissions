import heapq

class Solution:

    def leastInterval(self, tasks: List[str], n: int) -> int:
        heap = []
        queue = []

        freq_map = {}
        for task in tasks:
            if task not in freq_map:
                freq_map[task] = 0
            freq_map[task] += 1
        
        for elem, freq in freq_map.items():
            heap.append((-freq, elem))
        
        heapq.heapify(heap)

        t = 0

        while len(heap) > 0 or len(queue) > 0:
            t += 1
            if len(heap) > 0:
                freq, elem = heapq.heappop(heap)
                freq = -int(freq)
                if freq > 1:
                    queue.append((t + n , -(freq - 1), elem))
            

            # not sure if this ordering is right
            # will fix during debugging
            if len(queue) > 0:
                if queue[0][0] == t: # gives time
                    ready_time, freq, elem = queue.pop(0)
                    if ready_time > 0:
                        heapq.heappush(heap, (freq, elem))
            
        return t
            



        



       
        