
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
        if word == word[::-1] and self.root.idx is not None:
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
        empty = None
        for idx, w in enumerate(words):
            if len(w) == 0:
                empty = idx
            p = trie.isP(w, idx)
            if p is not None and p != idx:
                re.append([idx, p])
        if empty:
            em = list()
            for i in re:
                if i[1] == empty:
                    em.append([i[1],i[0]])
            re = re+em
        print(re)
        return re

s = Solution()
# s.palindromePairs(["abcd","dcba","lls","s","sssll"])
s.palindromePairs(["abcd","dcba","lls","s","sssll",""])

s.palindromePairs(["bat","tab","cat"])
s.palindromePairs(["a",""])
s.palindromePairs(["a","abc","aba",""])