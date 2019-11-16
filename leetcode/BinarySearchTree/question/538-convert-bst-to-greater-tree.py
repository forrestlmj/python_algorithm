# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    sum = 0
    def convertBST(self, root: TreeNode) -> TreeNode:
        def dfs(root):
            if not root:
                return None
            if root.right:
                dfs(root.right)
            root.val += self.sum
            self.sum = root.val
            if root.left:
              dfs(root.left)
            return self.sum
        self.sum = 0
        dfs(root)
        return root