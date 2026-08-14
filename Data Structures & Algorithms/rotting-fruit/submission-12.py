from collections import deque

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        num_1 = 0
        num_changed = 0
        visited_g = set()

        for row_1 in range(len(grid)):
            for col_1, elem in enumerate(grid[row_1]):
                if elem == 1:
                    num_1 += 1
        if num_1 == 0:
            return 0
            

        min_c = -1

        q = deque()
        
        for iter_row in range(len(grid)):
            for iter_col, elem in enumerate(grid[iter_row]):
                if elem == 2 and (iter_row, iter_col) not in visited_g:
                    # fruit is rotten, can start
                    q.append((iter_row, iter_col))
    
        c = 0


        init_len_q = len(q)

        # invariant: at each point, queue contains every rotten fruit that needs to spread

        while q:
            moved = False

            
            for _ in range(len(q)):
                row, col = q[_]
                grid[row][col] = 2
            
            for _ in range(len(q)):
                row, col = q.popleft()
                
                visited_g.add((row, col))

                if row + 1 < len(grid) and grid[row+1][col] == 1 and (row+1, col) not in visited_g:
                    moved = True
                    q.append((row+1, col))
                
                if row - 1 >= 0 and grid[row-1][col] == 1 and (row-1, col) not in visited_g:
                    moved = True
                    q.append((row-1, col))
                
                if col + 1 < len(grid[0]) and grid[row][col+1] == 1 and (row, col+1) not in visited_g:
                    moved = True
                    q.append((row, col+1))

                if col - 1 >= 0 and grid[row][col-1] == 1 and (row, col-1) not in visited_g:
                    moved = True
                    q.append((row, col - 1))
            if moved:
                c += 1
            
        min_c = max(min_c, c)
        if len(visited_g) - init_len_q != num_1:
            return -1
        return min_c