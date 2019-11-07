# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    max_depth = -1
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        self.dfs(root,0)

    def dfs(self,node,count):
        if not node:
            return count
        count1 = self.dfs(node.left,count+1)
        self.max_depth = max(count1,self.max_depth)
        count2 = self.dfs(node.right,count+1)
        self.max_depth = max(count2,self.max_depth)
        return self.max_depth
