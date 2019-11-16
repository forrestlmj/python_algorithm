# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    l = list()

    def increasingBST(self, root: TreeNode) -> TreeNode:
        if not root:
            return root
        def dfs(root):
            if not root:
                return
            if root.left:
                dfs(root.left)
            self.l.append(TreeNode(root.val))
            if root.right:
                dfs(root.right)
        self.l = list()
        dfs(root)
        for i in range(len(self.l)-1):
            self.l[i].right = self.l[i+1]
        return self.l[0]