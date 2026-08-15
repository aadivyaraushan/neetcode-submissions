from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        m = {}
        indegree = [0] * numCourses

        for prereq in prerequisites:
            after, before = prereq
            if before not in m:
                m[before] = []

            if after > numCourses or before > numCourses:
                return []
            
            m[before].append(after)
            indegree[after] += 1
        
        path = set()
        visited = set()

        def has_cycle(node):
            if node in path:
                return True
            if node in visited:
                return False
            
            path.add(node)
            visited.add(node)

            if node in m:
                for neighbor in m[node]:
                    if has_cycle(neighbor):
                        return True

            path.remove(node)
            return False
        
        for key, _ in m.items():
            if key not in visited:
                if has_cycle(key):
                    return []
        
        order = []

        # print(f"m: {m}")
        visited = set()

        if len(prerequisites) > 0:
            q = deque()
            for i in range(numCourses):
                if indegree[i] == 0:
                    visited.add(i)
                    q.append(i)

            while q:
                # print(f"q currently: {q}")
                elem = q.popleft()
                order.append(elem)
                
                if elem in m:
                    for nei in m[elem]:
                        indegree[nei] -= 1

                        if indegree[nei] == 0:
                            q.append(nei)
                            visited.add(nei)
        
        # print(f"post loop, order = {order}")
            
        total = set()
        for i in range(numCourses):
            total.add(i)
        
        remaining = total - visited

        for elem in remaining:
            order.append(elem)
        
        return order


        
        
                
            