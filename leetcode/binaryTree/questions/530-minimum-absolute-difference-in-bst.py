# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import sys
class Solution:
    pres = -sys.maxsize
    ans = sys.maxsize
    def getMinimumDifference(self, root: TreeNode) -> int:
        """
        解题思路依然是二叉搜索树的中序顺序是递增的，得到前一节点与当前节点的差值，获得最小值即可。
        """
        if not root:
            return 0
        def dfs(root):
            if not root:
                return
            if root.left:
                dfs(root.left)
            self.ans = min(self.ans,abs(root.val-self.pres))
            self.pres = root.val
            if root.right:
                dfs(root.right)
        self.pres = -sys.maxsize
        self.ans = sys.maxsize
        dfs(root)
        return self.ans