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
        # self.l = list()
        self.pre = -sys.maxsize
    def minDiffInBST(self, root: TreeNode) -> int:
        self.__init__()
        def dfs(root):
            if not root:
                return None
            if root.left:
                dfs(root.left)
            self.ans = min(self.ans,abs(root.val-self.pre))
            self.pre = root.val
            if root.right:
                dfs(root.right)
        dfs(root)

        return self.ans
"""
[7, 138, 263, 267, 296, 308, 322, 
362, 409, 496, 638, 703, 769, 808, 
883, 915, 945, 956, 961, 981]


"""