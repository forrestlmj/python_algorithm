# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return None
        return self.dfs(root,val)
    def dfs(self,cur,val):
        if cur:
            if cur.val == val:
                return cur

        if cur.left:
            v = self.dfs(cur.left,val)
            if v:
                return v
        if cur.right:
            v = self.dfs(cur.right,val)
            if v:
                return v
        return []