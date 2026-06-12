class PrefixNode:
    def __init__(self):
        self.is_end_of_word = False
        self.children = {} 
        

class PrefixTree:

    def __init__(self):
        self.root = PrefixNode()

    def insert(self, word: str) -> None:
        word_letters = list(word)
        curr = self.root
        while word_letters:
            char = word_letters[0]
            if char in curr.children:
                curr = curr.children[char]
            else:
                curr.children[char] = PrefixNode()
                curr = curr.children[char]
            word_letters.pop(0)
            if len(word_letters) == 0:
                curr.is_end_of_word = True


    def search(self, word: str) -> bool:
        word_letters = list(word)
        curr = self.root
        while word_letters:
            char = word_letters[0]

            if char not in curr.children:
                return False
            else:
                curr = curr.children[char]

            word_letters.pop(0)
            if len(word_letters) == 0 and curr.is_end_of_word:
                return True
        return False

    def startsWith(self, prefix: str) -> bool:
        prefix_letters = list(prefix)
        curr = self.root
        while prefix_letters:
            char = prefix_letters[0]

            if char not in curr.children:
                return False
            else:
                curr = curr.children[char]
            
            prefix_letters.pop(0)
        return True
