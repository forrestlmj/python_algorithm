# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def dfs(p,q):
            if not p and not q:
                return True
            elif p and q:
                return p.val == q.val and dfs(p.left,q.left) and dfs(p.right,q.right)
            else:
                return False
        return dfs(p,q)