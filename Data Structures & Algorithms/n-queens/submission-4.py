class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [['.'] * n for _ in range(n)]
        boards = []

        def is_valid_pos(row_n, col_n):
            for row_num, row in enumerate(board):
                for col_num, elem in enumerate(row):
                    if row_num == row_n and col_num == col_n:
                        continue
                    if elem == 'Q' and (row_num == row_n or col_num == col_n):
                        return False
                    if elem == 'Q' and (row_num - col_num == row_n - col_n or row_num + col_num == row_n + col_n):
                        return False
            return True
            # quick check: 
            # yes this is correct can confirm did a mental check
            # assume this is correct

        def backtrack(row):
            # meaning: backtrack(row) checks 
            # an entire row for a given prior queen position
            # to see if we can place a queen in this new row
            # in a way thats compatible with the prior row
            nonlocal boards
            if row == n:
                # found an entire valid board
                boards.append(["".join(row) for row in board])
                return
            
            # print(f"inspecting board")

            found_validity = False
            for col, char in enumerate(board[row]):
                if is_valid_pos(row, col):
                    board[row][col] = 'Q'
                    # print(f"board pre backtracking: {board}")
                    backtrack(row+1)
                    board[row][col] = '.'
                    # print(f"board post backtracking: {board}")
                    found_validity = True
                    # print(f"found validity")
            
            if not found_validity:
                # print(f"didn't find any validity")
                return

        backtrack(0)
        return boards
