# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        def dfs(root):
            if not root:
                return None
            l = list()
            if not root.left and not root.right:
                return [root.val]
            if root.left:
                l = l+dfs(root.left)
            if root.right:
                l = l+dfs(root.right)
            return l
        l1 = dfs(root1)
        l2 = dfs(root2)
        print(l1)
        print(l2)
        return l1.__eq__(l2)