from collections import deque

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # algo key idea:
        # initialize a 2d array of size same as heights 
        # do BFS from topmost row points, leftmost col points
        # seeing all cells where you can have height >= curr height continuously
        # mark those as benig reachable by pacific 
        # do that by setting that val to a tuple that has (pacific_val, false) stored there

        # same thing for bottommost row, rightmost col points
        # those are reachable by atlantic
        # to mark that set [1] of tuple to true

        # finally at end iterate through heights and 
        # have an output list, appending any index where both are true
        # to that list

        reachability = []
        for i in range(len(heights)):
            row = []
            for j in range(len(heights[0])):
                row.append([False, False])
            reachability.append(row)

        
        q = deque()
        visited = set()
        for i in range(len(heights[0])):
            q.append((0, i))
            visited.add((0, i))

        for j in range(1, len(heights)):
            q.append((j, 0))
            visited.add((j, 0))
        
        while q:
            row, col = q.popleft()
            reachability[row][col][0] = True

            if row+1 < len(heights) and heights[row+1][col] >= heights[row][col] and (row+1, col) not in visited:
                q.append((row+1, col))
                visited.add((row+1, col))

            if row-1 >= 0 and heights[row-1][col] >= heights[row][col] and (row-1, col) not in visited:
                q.append((row-1, col))
                visited.add((row-1, col))

            
            # might contain (1, 4) preventing transition

            if col+1 < len(heights[0]) and heights[row][col+1] >= heights[row][col] and (row, col+1) not in visited:
                q.append((row, col+1))
                visited.add((row, col+1))

            if col-1 >= 0 and heights[row][col-1] >= heights[row][col] and (row, col-1) not in visited:
                q.append((row, col-1))
                visited.add((row, col-1))
        
        q = deque()
        visited = set()
        # rightmost column
        for i in range(len(heights)):
            q.append((i, len(heights[0]) - 1))
            visited.add((i, len(heights[0]) - 1))
        
        # bottommostrow
        for j in range(0, len(heights[0]) - 1):
            q.append((len(heights)-1, j))
            visited.add((len(heights)-1, j))
        
        
        while q:
            row, col = q.popleft()
            reachability[row][col][1] = True

            if row+1 < len(heights) and heights[row+1][col] >= heights[row][col] and (row+1, col) not in visited:
                q.append((row+1, col))
                visited.add((row+1, col))

            if row-1 >= 0 and heights[row-1][col] >= heights[row][col] and (row-1, col) not in visited:
                q.append((row-1, col))
                visited.add((row-1, col))

            if col+1 < len(heights[0]) and heights[row][col+1] >= heights[row][col] and (row, col+1) not in visited:
                q.append((row, col+1))
                visited.add((row, col+1))

            if col-1 >= 0 and heights[row][col-1] >= heights[row][col] and (row, col-1) not in visited:
                q.append((row, col-1))
                visited.add((row, col-1))
        
        output = []
        for row_num in range(len(reachability)):
            for col_num in range(len(reachability[0])):
                if reachability[row_num][col_num][0] and reachability[row_num][col_num][1]:
                    output.append((row_num, col_num))
        
        return output
            
            
