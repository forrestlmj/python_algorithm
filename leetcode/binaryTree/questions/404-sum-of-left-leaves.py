# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    ans = 0
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return None
            if not root.left and not root.right:
                return root
            if root.left:
                a = dfs(root.left)
                if a:
                    self.ans += a.val
            if root.right:
                dfs(root.right)
        self.ans = 0
        dfs(root)
        return self.ans