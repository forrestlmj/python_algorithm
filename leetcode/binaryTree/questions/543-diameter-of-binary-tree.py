# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    max_l = 0
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        if not root :
            return 0
        self.dfs(root)
        return self.max_l
    def dfs(self,cur):
        # cur_l = ((1+maxl) if maxl )+((1+maxr) if maxr)
        # max_l = max(max_l,cur_l)
        if not cur.left and not cur.right:
            return 0
        l = 0
        if cur.left:
            l += self.dfs(cur.left)+1
        r = 0
        if cur.right:
            r += self.dfs(cur.right)+1
        self.max_l = max(self.max_l,l+r)
        return max(l,r)