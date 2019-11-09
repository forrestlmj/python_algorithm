# Definition for a binary tree node.
import math
import queue


class TreeNode(object):
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        a = self.dfs(root,p.val)
        b = self.dfs(root,q.val)
        re = None
        for i in range(min(len(a),len(b))):
            if a[i] == b[i]:
                re = a[i]
            else:
                break
        print(re)
        return re
    def dfs(self,cur,q):
        """

        :return: list
        """
        if cur:
            if cur.val == q:
                return [cur.val]
            else:
                left = self.dfs(cur.left,q)
                if left:
                    #
                    return [cur.val]+left
                right = self.dfs(cur.right,q)
                if right:
                    return [cur.val]+right
s = Solution()
s.lowestCommonAncestor(
    TreeNode(3,
       TreeNode(5,
            TreeNode(6,None,None),
            TreeNode(2,TreeNode(7,None,None),TreeNode(4,None,None))
            ),
        TreeNode(1,
             TreeNode(0,None,None),
             TreeNode(8, None, None),
             ),
       )
    ,TreeNode(5,None,None),TreeNode(1,None,None)
)
s.lowestCommonAncestor(
    TreeNode(3,
       TreeNode(5,
            TreeNode(6,None,None),
            TreeNode(2,TreeNode(7,None,None),TreeNode(4,None,None))
            ),
        TreeNode(1,
             TreeNode(0,None,None),
             TreeNode(8, None, None),
             ),
       )
    ,TreeNode(5,None,None),TreeNode(4,None,None)
)
a = 1
