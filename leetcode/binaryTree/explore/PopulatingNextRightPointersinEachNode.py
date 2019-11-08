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
    def islog2(self, n):
        return math.log2(n).is_integer()
    def linkQueue(self,q):
        for i in range(len(q)-1):
            q[i].next = q[i+1]
        return
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        d_r = Node(None,None,None,root)
        q = queue.deque()
        pop_count = 0
        q.append(root)
        while len(q)>0:
            cur = q.popleft()
            if cur:
                pop_count += 1
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                if self.islog2(pop_count+1):
                    self.linkQueue(q)
        return d_r.next

s = Solution()
s.connect(
    Node(1,
       Node(2,
            Node(4,None,None,None),
            Node(5,None,None,None),
            None),
        Node(3,
             Node(6, None, None, None),
             Node(7, None, None, None),
             None),
       None)
)
a = 1
