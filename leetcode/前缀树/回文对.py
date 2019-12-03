
class Node:
    def __init__(self):
        self.idx = None
        self.next = dict()


class Trie:
    def __init__(self):
        self.root = Node()

    def insert(self, word, idx):
        node = self.root
        for i in word[::-1]:
            if not node.next.get(i):
                node.next[i] = Node()
            node = node.next.get(i)
        node.idx = idx

    def isP(self, word, idx):
        node = self.root
        # if not word:
        #     return idx
        if word and self.root.idx is not None:
            return self.root.idx
        for i in word:
            if not node.next.get(i):
                return
            node = node.next.get(i)
        while node:
            if node.idx is not None and idx != node.idx:
                return node.idx
            elif len(list(node.next.values()))>0:
                node = list(node.next.values())[0]
            else:
                break

        return


class Solution:
    def palindromePairs(self, words: [str]) -> [[int]]:
        trie = Trie()
        for idx, w in enumerate(words):
            trie.insert(w, idx)
        re = list()
        for idx, w in enumerate(words):
            p = trie.isP(w, idx)
            if p is not None and p != idx:
                re.append([idx, p])
        print(re)
        return re
