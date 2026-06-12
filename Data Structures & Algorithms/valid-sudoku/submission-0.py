class Solution:

    def has_duplicates(self, arr):
        has_appeared_set = []
        for elem in arr:
            print(f"elem inspected: {elem}")
            if elem in has_appeared_set and elem != '.':
                print ("elem has alr appeared")
                return True
            has_appeared_set.append(elem)
        return False

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # checking if each row has no duplicates
        # True by default, if any has duplicates becomes False
        # stays that way is never set again
        for row in board:
            print(f'currently inspecting row: {row}')
            if self.has_duplicates(row):
                return False

        # checking if each col has no duplicates
        # True by default, if any has duplicates becomes False
        # stays that way is never set again
        num_cols = len(board[0])
        for col_num in range(num_cols):
            col = []
            print('generating col')
            for i in range(len(board)):
                col.append(board[i][col_num])
                print(f'adding {board[i][col_num]} to col')
            if self.has_duplicates(col):
                return False
    
        for i in range(0, 9, 3): # col
            for j in range(0, 9, 3): # row
                elems_in_3x3 = []
                for k in range(i, i+3): # col inside 3x3
                    for m in range(j, j+3): # row inside 3x3
                        print (f'in 3x3, inspecting: {board[k][m]}')
                        elems_in_3x3.append(board[k][m])
                print('end of one 3x3')
                print(f'elems in 3x3 is now: {elems_in_3x3}')
                if self.has_duplicates(elems_in_3x3):
                    return False
        
        return True



