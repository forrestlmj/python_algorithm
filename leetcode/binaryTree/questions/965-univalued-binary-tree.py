# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x,left,right):
        self.val = x
        self.left = left
        self.right = right


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if not root:
            return False
        root_val = root.val
        return self.in_order_dfs(root,root_val)
    def in_order_dfs(self,cur,root_val):
        if not cur.left and not cur.right:
            return cur.val == root_val
        if root_val != cur.val:
            return False
        if cur.left:
            if not self.in_order_dfs(cur.left,root_val):
                return False
        if cur.right:
            if not self.in_order_dfs(cur.right,root_val):
                return False
        return True
import queue

def test():
    s = Solution()
    print(s.isUnivalTree(
        TreeNode(1,
                 TreeNode(1,
                          TreeNode(1,None,None),
                          TreeNode(1,None,None)
                          ),
                 TreeNode(1,
                          None,
                          TreeNode(2,None,None)
                          )
                 )
    ))
if __name__ == "__main__":
    test()