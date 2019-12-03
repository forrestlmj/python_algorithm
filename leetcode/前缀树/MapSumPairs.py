# -*- coding: utf-8 -*- 
# @Time : 2019/12/1 下午8:26 
# @Author : yangchengkai
# @File : MapSumPairs.py
# https://leetcode-cn.com/explore/learn/card/trie/167/practical-application-i/647/
class Node:
    def __init__(self, value=0):
        self.value = value
        self.isWord = False
        self.next = dict()


class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()

    def reset(self, key, val, add=True):
        node = self.root
        for k in key:
            node.next[k].value = val + (node.next[k].value if add else 0)
            node = node.next[k]

    def insert(self, key: str, val: int) -> None:
        node = self.root
        for k in key:
            # print(k)
            if not node.next.get(k):
                node.next[k] = Node()
            node = node.next[k]
        if not node.isWord:
            self.reset(key, val, add=True)
        else:
            self.reset(key, val, add=False)
        node.isWord = True

    def sum(self, prefix: str) -> int:
        node = self.root

        for p in prefix:
            if not node.next.get(p):
                return 0
            node = node.next[p]
        return node.value

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)