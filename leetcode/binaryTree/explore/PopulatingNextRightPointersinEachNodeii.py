# Definition for a binary tree node.
import math
import queue


class Node(object):
    def __init__(self, val, left, right, next):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
class Solution(object):

    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        q = queue.deque()
        d_r = Node(None,None,None,root)
        l = dict()
        q.append((root, 0))
        while len(q) > 0:
            cur,level = q.popleft()
            if cur:
                if level in l:
                    l[level].append(cur)
                else:
                    l[level] = [cur]
                if cur.left:
                    q.append((cur.left,level+1))
                if cur.right:
                    q.append((cur.right,level+1))
        for level in l.values():
            for i in range(len(level)-1):
                level[i].next = level[i+1]
        a = 1
        return d_r.next
s = Solution()
s.connect(
    Node(1,
       Node(2,
            Node(4,None,None,None),
            Node(5,None,None,None),
            None),
        Node(3,
             None,
             Node(7, None, None, None),
             None),
       None)
)
a = 1
