"""
This is a try data structure used for auto complete and stuff
"""


class TrieNode:

    def __init__(self, char="") -> None:
        self.char = char
        self.children = dict()
        self.is_end = False


class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root

        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                new_node = TrieNode(char)
                node.children[char] = new_node
                node = new_node
        node.is_end = True

    
    def search(self, word):
        node = self.root
        
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False

        return node.is_end
    
    def startswith(self, word):
        node = self.root
        
        for char in word:
            if char in node.children:
                node = node.children[char]
            else:
                return False

        return True

