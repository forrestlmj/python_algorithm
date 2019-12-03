import queue


class Node:
    def __init__(self):
        self.isWord = False
        self.next = dict()


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        node = self.root
        for i in word:
            if not node.next.get(i):
                node.next[i] = Node()
            node = node.next[i]
        node.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """

        # node = self.root

        def helper(node, word):
            if not word:
                return node.isWord
            if word[0] == '.':
                for i in node.next.values():
                    if helper(i, word[1:]):
                        return True
                return False
            else:
                if not node.next.get(word[0]):
                    return False
                return helper(node.next.get(word[0]), word[1:])

        return helper(self.root, word)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)