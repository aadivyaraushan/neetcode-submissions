class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:

        board = [['.'] * n for _ in range(n)]
        boards = []
        cols = set()
        diagonals = set()
        diagonals2 = set()

        def is_valid_pos(row_n, col_n):
            return col_n not in cols and (row_n - col_n) not in diagonals and (row_n + col_n) not in diagonals2
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
                    cols.add(col)
                    diagonals.add(row - col)
                    diagonals2.add(row + col)
                    # print(f"board pre backtracking: {board}")
                    backtrack(row+1)
                    board[row][col] = '.'
                    cols.remove(col)
                    diagonals.remove(row - col)
                    diagonals2.remove(row + col)
                    # print(f"board post backtracking: {board}")
                    found_validity = True
                    # print(f"found validity")
            
            if not found_validity:
                # print(f"didn't find any validity")
                return

        backtrack(0)
        return boards
