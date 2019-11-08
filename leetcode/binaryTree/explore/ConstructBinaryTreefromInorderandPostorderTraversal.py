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
        node = None
        while len(postorder)>1:
            c = postorder.pop()
            node = TreeNode(c)
            node.right = TreeNode(self.buildTree(inorder,postorder) if self.buildTree(inorder,postorder) else None)
            self.seen.add(c)

            node.left = TreeNode(self.buildTree(inorder[inorder.index(c)-1:],postorder))
            pass
            pass
        return TreeNode(postorder.pop())
s = Solution()
s.buildTree([9,3,15,20,7],[9,15,7,20,3])