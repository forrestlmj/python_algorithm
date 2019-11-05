# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        re = list()
        self.dfs(root,re)
        return re
    def dfs(self,root,re):
        if root:
            self.dfs(root.left,re)
            re.append(root.val)
            self.dfs(root.right,re)
