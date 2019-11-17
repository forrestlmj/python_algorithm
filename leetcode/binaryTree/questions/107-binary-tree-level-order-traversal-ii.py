# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import queue
class Solution:
    def levelOrderBottom(self, root: TreeNode) :
        q = queue.deque()
        r = list()
        if not root:
            return []
        q.append((root,0))
        while q:
            (cur,level) = q.popleft()
            if level == len(r):
                r.append([cur.val])
            else:
                r[level].append(cur.val)
            if cur.left:
                q.append((cur.left,level+1))
            if cur.right:
                q.append((cur.right,level+1))
        return r[::-1]