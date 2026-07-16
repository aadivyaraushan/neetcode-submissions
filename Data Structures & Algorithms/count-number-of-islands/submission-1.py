class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = []
        for row in grid:
            visited.append([False] * len(row))
        components = 0

        def dfs(row, col):
            # check all 4 directions and if any are land, continue dfs
            # from there and set those to be true 

            if row < 0 or row >= len(grid):
                return
            if col < 0 or col >= len(grid[0]):
                return
            if visited[row][col]:
                return
            
            if grid[row][col] == '1':
                visited[row][col] = True
            else:
                return

            dfs(row+1, col)
            dfs(row, col+1)
            dfs(row, col-1)
            dfs(row-1, col)


        for row, row_elems in enumerate(grid):
            for col, is_land in enumerate(row_elems):
                if not visited[row][col] and is_land == '1':
                    components += 1 
                    dfs(row, col)


        return components