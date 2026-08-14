from collections import deque

class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        q = deque()
        visited = set()
        for row_i in range(len(grid)):
            for col_i in range(len(grid[row_i])):
                if grid[row_i][col_i] == 0:
                    q.append((row_i, col_i))
                    visited.add((row_i, col_i))

        c = 0    
        while q:
            for _ in range(len(q)):
                row, col = q.popleft()
                grid[row][col] = c

                if row - 1 >= 0 and (row-1, col) not in visited and grid[row-1][col] == 2**31 - 1:
                    visited.add((row-1, col))
                    q.append((row-1, col))
                
                if col - 1 >=0 and (row, col-1) not in visited and grid[row][col-1] == 2**31 - 1:
                    visited.add((row, col-1))
                    q.append((row, col-1))
                
                if row + 1 < len(grid) and (row+1, col) not in visited and grid[row+1][col] == 2**31 - 1:
                    visited.add((row+1, col))
                    q.append((row+1, col))
                
                if col + 1 < len(grid[0]) and (row, col+1) not in visited and grid[row][col+1] == 2**31 - 1:
                    visited.add((row, col+1))
                    q.append((row, col+1))

            c += 1