# Definition for a binary tree node.
import sys


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    ans,l = None,None
    def __init__(self):
        self.ans = sys.maxsize
        self.l = list()
    def minDiffInBST(self, root: TreeNode) -> int:
        self.__init__()
        def dfs(root):
            if not root:
                return None
            if root.left:
                dfs(root.left)
                # self.l.append(root.left.val)
                # self.ans = min(self.ans,root.val-root.left.val)
            self.l.append(root.val)
            if root.right:
                dfs(root.right)
                # self.ans = min(self.ans,abs(root.val-root.right.val))
                # self.l.append(root.right.val)
        dfs(root)
        print(self.l)
        for i in range(0,len(self.l)-1):
            self.ans = min(self.ans,self.l[i+1]-self.l[i])
        return self.ans
"""
[7, 138, 263, 267, 296, 308, 322, 
362, 409, 496, 638, 703, 769, 808, 
883, 915, 945, 956, 961, 981]


"""