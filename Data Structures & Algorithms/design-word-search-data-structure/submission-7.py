class TrieNode:
    def __init__(self, char, is_word, children):
        self.is_word = is_word
        self.char = char
        self.children = children # array of trie nodes

class WordDictionary:

    def __init__(self):
        self.root = TrieNode('', False, [])

    def addWord(self, word: str) -> None:
        node = self.root
        chars = list(word) # works because O(L)
        while len(chars) > 0:
            char = chars.pop(0)
            found = False
            for child in node.children:
                if child.char == char:
                    node = child
                    found = True
            if not found:
                new_node = TrieNode(char, False, [])
                node.children.append(new_node)
                node = new_node
        # print(f"final node char: {node.char}")
        node.is_word = True


    def search(self, word: str) -> bool:
        # print(f"\n\ncalling search({word})")
        def recursive(chars, node):
            # print(f"\ncalling recursive({chars}, node: char = {node.char}, children = {[child.char for child in node.children]}")

            if len(chars) == 0:
                return node.is_word

            char = chars.pop(0)

            if char == '.':
                # print(f". path")
                if len(node.children) == 0:
                    return False
                outcome = recursive(chars.copy(), node.children[0])
                for child in node.children[1:]:
                    outcome = outcome or recursive(chars, child)
                return outcome 
            for child in node.children:
                if child.char == char:
                    # print(f"child storing {char} found. setting node to child")
                    node = child
                    return recursive(chars, node)
            
            return False
            

        return recursive(list(word), self.root)