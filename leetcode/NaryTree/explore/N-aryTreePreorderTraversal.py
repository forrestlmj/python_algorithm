
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

# import builtins.List

class Solution:
    def preorder(self, root: 'Node'):
        if not root:
            return None

        q = list()
        l = list()
        q.append(root)
        while len(q) >0:
            cur = q.pop()
            l.append(cur.val)
            if not cur.children:
                continue
            for i in cur.children[::-1]:
                if i:
                    q.append(i)
        return l
