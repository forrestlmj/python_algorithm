
# Definition for a Node.
class Node:
    def __init__(self, val, children):
        self.val = val
        self.children = children

# import builtins.List
class Solution:
    def postorder(self,root):
        if not root:
            return None
        l = list()
        s = list()
        s.append(root)
        while len(s) > 0:
            cur = s.pop()
            if cur:
                l.append(cur.val)
                for c in cur.children:
                    s.append(c)
        return l[::-1]
