class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        area = 0
        visited = []
        for row_num in range(len(grid)):
            visited.append([False] * len(grid[0]))
        
        def dfs(row, col):
            nonlocal max_area
            nonlocal area


            if row < 0 or row >= len(grid):
                return
            if col < 0 or col >= len(grid[0]):
                return
            if visited[row][col]:
                return
            if grid[row][col] == 0:
                return
            
            area += 1 
            visited[row][col] = True
            dfs(row + 1, col)
            dfs (row, col + 1)
            dfs(row - 1, col)
            dfs(row, col - 1)

        for row, row_elems in enumerate(grid):
            for col, is_land in enumerate(row_elems):
                if not visited[row][col] and is_land == 1:
                    area = 0
                    dfs(row, col)
                    max_area = max(max_area, area)
        
        return max_area

