# # Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x,left,right):
#         self.val = x
#         self.left = left
#         self.right = right
#

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        c = TreeNode(None)
        if not root:
            return None
        self.dfs(root)
        return root
    def dfs(self,cur):
        if not cur.left and not cur.right:
            return
        tmp = TreeNode(None)
        tmp = cur.left
        cur.left = cur.right
        cur.right = tmp
        if cur.right:
            self.dfs(cur.right)
        if cur.left:
            self.dfs(cur.left)
#
# # str
# def test():
#     s = Solution()
#     print(
#         s.findTilt(
#             TreeNode(1,TreeNode(2,None,None),TreeNode(1,None,None))
#         )
#     )
#     print(s.findTilt(
#         TreeNode(1,
#                  TreeNode(1,
#                           TreeNode(1,None,None),
#                           TreeNode(1,None,None)
#                           ),
#                  TreeNode(1,
#                           None,
#                           TreeNode(1,None,None)
#                           )
#                  )
#     ))
# if __name__ == "__main__":
#     test()