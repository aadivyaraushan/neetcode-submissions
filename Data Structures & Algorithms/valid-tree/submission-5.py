from collections import deque

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        m = {}
        for edge in edges:
            before, after = edge
            if before not in m:
                m[before] = []
            m[before].append(after)

            if after not in m:
                m[after] = []
            m[after].append(before)
        

        q = deque()
        visited = set()
        q.append(0)
        visited.add(0)
        
        if len(edges) > 0:
            while q:
                # print(f"in current iter, q = {q}")
                node = q.popleft()

                for neigh in m[node]:
                    if neigh not in visited:
                        visited.add(neigh)
                        q.append(neigh)    


        return len(visited) == n



        

