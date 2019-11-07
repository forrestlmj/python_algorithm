# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import queue
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        r = list()
        q = queue.deque()
        q.append((root,0))
        # d = dict()
        while len(q) > 0:
            cur,level = q.popleft()
            if level == len(r):
                r.append([])
                r[level].append(cur.val)
            else:
                r[level].append(cur.val)
            if cur.left:
                q.append((cur.left,level+1))
            if cur.right:
                q.append((cur.right,level+1))

        return r
def test():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(3)
    d = TreeNode(4)
    e = TreeNode(5)
    a.left = b
    a.right = c
    b.left = d
    c.right = e
    s = Solution()
    print(s.levelOrder(a))
test()