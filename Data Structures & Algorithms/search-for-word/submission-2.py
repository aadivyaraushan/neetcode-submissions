class Solution:

    def exist(self, board: List[List[str]], word: str) -> bool:
        rows = len(board)
        cols = len(board[0])

        def dfs(row, col, i):
            if i == len(word):
                return True
            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] != word[i]:
                return False
            
            temp = board[row][col]
            board[row][col] = '#'

            found = dfs(row+1, col, i+1) or dfs(row, col+1, i+1) or dfs(row-1, col, i+1) or dfs(row, col-1, i+1)

            board[row][col] = temp
            return found
        
        for row in range(rows):
            for col in range(cols):
                if dfs(row, col, 0):
                    return True
        return False