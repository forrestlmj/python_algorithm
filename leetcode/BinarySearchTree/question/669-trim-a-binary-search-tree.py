# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        def dfs(cur):
            if not cur:
                return
            if cur.val < L:
                return dfs(cur.right)
            if cur.val > R:
                return dfs(cur.left)
            cur.left = dfs(cur.left)
            cur.right = dfs(cur.right)
            return cur
        return dfs(root)