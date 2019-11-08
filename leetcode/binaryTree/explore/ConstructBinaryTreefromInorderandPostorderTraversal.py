# Definition for a binary tree node.
# class TreeNode(object):
#     # def __init__(self, x):
#     #     self.val = x
#     #     self.left = None
#     #     self.right = None
#     def __init__(self,x,left,right):
#         self.val = x
#         self.left = left
#         self.right = right


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    seen = set()
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """
        if not inorder or not postorder:
            return None
        root = TreeNode(postorder.pop())
        inorderindex = inorder.index(root.val)
        root.right = self.buildTree(inorder[inorderindex+1:],postorder)
        root.left = self.buildTree(inorder[:inorderindex],postorder)
        return root
s = Solution()
s.buildTree([9,3,15,20,7],[9,15,7,20,3])