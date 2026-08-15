from collections import deque

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = [0]
        for i in range(1, len(edges) + 1):
            parent.append(i)
        rank = [0] * (len(edges)+1)

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            
            return parent[x]
        
        def union(x, y):
            # checks if two share the same parent. if they do,
            # returns True
            # if not, returns False and combines parents
            rx = find(x)
            ry = find(y)
            if rx == ry:
                return True
            
            if rank[rx] > rank[ry]:
                parent[ry] = rx
            elif rank[rx] < rank[ry]:
                parent[rx] = ry
            else:
                parent[rx] = ry
                rank[ry] += 1
            

            return False
            

        ans = []
        for edge in edges:
            before, after = edge
            if find(before) == find(after):
                ans = edge
            union(before, after)

            # print(f"now, parent = {parent}")

            
        return ans
        
