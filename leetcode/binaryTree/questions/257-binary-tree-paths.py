# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    ans = list()
    def binaryTreePaths(self, root: TreeNode) -> [str]:
        if not root:
            return []
        def dfs(root,p):
            if not root:
                return
            if not root.left and not root.right:
                p.append(str(root.val))
                self.ans.append("->".join(p))
                return
            dfs(root.left,p+[str(root.val)])
            dfs(root.right,p+[str(root.val)])
        self.ans = list()
        dfs(root,[])
        return self.ans