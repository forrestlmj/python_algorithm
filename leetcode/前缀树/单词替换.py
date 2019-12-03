# -*- coding: utf-8 -*- 
# @Time : 2019/12/1 下午9:02 
# @Author : yangchengkai
# @File : 单词替换.py
class Node:
    def __init__(self):
        self.isWord = False
        self.next = dict()
class Trie:
    def __init__(self):
        self.root = Node()
    def insert(self,key):
        node = self.root
        for i in key:
            if not node.next.get(i):
                node.next[i] = Node()
            node = node.next.get(i)
        node.isWord = True
    def prefix(self,key):
        node = self.root
        for i in range(len(key)):
            if not node.next.get(key[i]):
                return key
            else:
                if node.next.get(key[i]).isWord:
                    return key[:i+1]
            node = node.next.get(key[i])
        return key
class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        """
        典型的字典树解法，时间复杂度：Time O(N)
        如果暴力解法：Time O(N^2)，字典长度*语句中单词长度
        """
        trie = Trie()
        for i in dict:
            trie.insert(i)
        re = []
        for i in sentence.split(" "):
            re.append(trie.prefix(i))
            print(trie.prefix(i))
        return " ".join(re)