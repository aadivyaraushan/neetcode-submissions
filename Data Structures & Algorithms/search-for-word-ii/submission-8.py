class Solution:
    
    
    class Trie:
        class TrieNode:
            def __init__(self, char, children_chars, is_word):
                self.char = char
                self.children = {}
                for child in children_chars:
                    self.children[child] = TrieNode('', [])
                self.is_word = is_word

        def __init__(self):
            self.root = self.TrieNode('', [], False)
        
        def add(self, word):
            node = self.root
            chars = list(word[::-1])
            while len(chars) > 0:
                char = chars.pop()
                if char not in node.children:
                    node.children[char] = self.TrieNode('', [], False)
                    node = node.children[char]
                else:
                    node = node.children[char]
            node.is_word = True

        
        



    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        t = self.Trie()
        node = t.root
        i = 0
        j = 0
        
        output = []
        path = []
        
        for word in words:
            t.add(word)

        visited = set()

        def backtrack(row, col, node):
            nonlocal output
            nonlocal visited
            # print(f"after backtrack({row}, {col}), path = {path}")

            

            if node.is_word and "".join(path) not in output:
                output.append("".join(path))
            
            
            left = (row, col - 1)
            down = (row + 1, col)
            up = (row - 1, col)
            right = (row, col + 1)

            directions = [left, down, up, right]
            # print(f"right now, directions = {directions}")
            # print(f"meanwhile, visited = {visited}")
            for direction in directions:
                row = direction[0]
                col = direction[1]
                # print(f"row: {row}, col: {col}")
 
                if row >= 0 and row < len(board) and col >= 0 and col < len(board[0]):
                    if board[row][col] in node.children and (row, col) not in visited:
                        # print(f"calling backtrack within backtrack function")
                        visited.add((row, col))
                        path.append(board[row][col])
                        backtrack(row, col, node.children[board[row][col]])
                        visited.remove((row, col))
                        path.pop()
        for row in range(len(board)):
            for col in range(len(board[0])):
                if board[row][col] in node.children:
                    path.append(board[row][col])
                    visited.add((row, col))
                    backtrack(row, col, node.children[board[row][col]])
                    visited.remove((row, col))
                    path.pop()

        # print(f"len(output): {len(output)}")
        # print(f"len(set(output)): {len(set(output))}")

        return output




