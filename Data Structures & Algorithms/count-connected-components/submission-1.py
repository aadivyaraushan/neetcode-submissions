from collections import deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        m = {}
        for i in range(n):
            m[i] = []
        for edge in edges:
            before, after = edge

            m[before].append(after)
            m[after].append(before)
        
        q = deque()
        visited = set()

        def bfs(node):
            nonlocal q
            nonlocal visited

            q.append(node)
            visited.add(node)

            while q:
                elem = q.popleft()

                for neigh in m[elem]:
                    if neigh not in visited:
                        visited.add(neigh)
                        q.append(neigh)
        
        c = 0
        for i in range(n):
            if i not in visited:
                bfs(i)
                c += 1
        
        return c