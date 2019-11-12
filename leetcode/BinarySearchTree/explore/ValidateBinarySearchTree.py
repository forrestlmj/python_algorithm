# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if not root:
            return True
        return self.dfs(root)
    def dfs(self,cur,low = float('-inf'),high = float('inf')):
        if not cur:
            return True
        if cur.val <= low or cur.val >= high:
            return False
        if not self.dfs(cur.right,cur.val,high):
            return False
        if not self.dfs(cur.left,low,cur.val):
            return False
        return True