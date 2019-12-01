# -*- coding: utf-8 -*- 
# @Time : 2019/11/30 下午10:58 
# @Author : yangchengkai
# @File : 实现 Trie (前缀树).py
# https://leetcode-cn.com/explore/learn/card/trie/166/basic-operations/645/


class Node:
    def __init__(self):
        """
        节点的数据结构为下一连接，以及root到当前节点是否是一个单词。next值可以使用动态链表或者字典都可以。这里用的字典存储下一个地址
        """
        self.isWord = False
        self.next = dict()


class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        node = self.root
        for i in word:
            if not node.next.get(i):
                node.next[i] = Node()
            node = node.next[i]
        node.isWord = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        node = self.root
        for i in word:
            if not node.next.get(i):
                return False
            node = node.next[i]
        return node.isWord

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        node = self.root
        for i in prefix:
            if not node.next.get(i):
                return False
            node = node.next[i]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)