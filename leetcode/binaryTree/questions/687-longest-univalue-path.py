# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x,l,r):
        self.val = x
        self.left = l
        self.right = r

class Solution:
    def longestUnivaluePath(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return 0
            l,r = 0,0
            if root.left:
                if root.left.val == root.val:
                    l += 1
                l = dfs(root.left)
            if root.right:
                if root.right.val == root.val:
                    r += 1
                r = dfs(root.right)
            if root.left and root.right:
                if root.val == root.left.val and root.val ==root.right.val:
                    return l+r
            else:
                return max(l,r)
        return dfs(root)

s = Solution()
print(s.longestUnivaluePath(
    TreeNode(5,
             TreeNode(4,TreeNode(4,None,None),TreeNode(4,None,None)),
             TreeNode(5,None,TreeNode(5,None,None)))
))
