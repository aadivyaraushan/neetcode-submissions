from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        m = {}

        for i in range(len(prerequisites)):
            after, before = prerequisites[i]

            if (after in m and before in m[after]) or after == before:
                # print(f"pre false return, m = {m}")
                return False
            if after > numCourses or before > numCourses:
                # print(f"pre false return, m = {m}")
                return False
            
            if before not in m:
                m[before] = []
            m[before].append(after)

        
        visited = set()
        path = set()

        def has_cycle(node):
            # print(f"in call has_cycle({node}), path = {path} and visited = {visited}")
            if node in path:
                return True
            if node in visited:
                return False
            
            visited.add(node)
            path.add(node)

            if node in m:
                for neighbor in m[node]:
                    if has_cycle(neighbor):
                        return True
            
            path.remove(node)
            return False
        
        
        if len(prerequisites) > 0:
            for key, _ in m.items():
                if key not in visited and has_cycle(key):
                    return False
        
        return True