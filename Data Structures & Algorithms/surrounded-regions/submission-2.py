from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        visited = set()
        regions = []

        for row_num in range(len(board)):
            for col_num in range(len(board[0])):
                if (row_num, col_num) not in visited:
                    visited.add((row_num, col_num))
                    if board[row_num][col_num] == 'O':
                        region = []
                        q = deque()

                        q.append((row_num, col_num))

                        while q:
                            row, col = q.popleft()
                            region.append((row, col))
                            

                            if row+1 < len(board) and board[row+1][col] == 'O' and (row+1, col) not in visited:
                                q.append((row+1, col))
                                visited.add((row+1, col))
                            
                            if col+1 < len(board[0]) and board[row][col+1] == 'O' and (row, col+1) not in visited:
                                q.append((row, col+1))
                                visited.add((row, col+1))
                            
                            if row-1 >= 0 and board[row-1][col] == 'O' and (row-1, col) not in visited:
                                q.append((row-1, col))
                                visited.add((row-1, col))
                            
                            if col - 1 >= 0 and board[row][col-1] == 'O' and (row, col-1) not in visited:
                                q.append((row, col-1))
                                visited.add((row, col-1))
                        regions.append(region)
        
        for region in regions:
            at_border = False
            for elem in region:
                row_r, col_r = elem
                if row_r == 0 or row_r == len(board) - 1:
                    at_border = True
                
                if col_r == 0 or col_r == len(board[0]) - 1:
                    at_border = True
            if not at_border:
                for elem in region:
                    row_r, col_r = elem
                    board[row_r][col_r] = 'X'


                
                