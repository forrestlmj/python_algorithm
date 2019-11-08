# Definition for a binary tree node.
class TreeNode(object):
    # def __init__(self, x):
    #     self.val = x
    #     self.left = None
    #     self.right = None
    def __init__(self,x,left,right):
        self.val = x
        self.left = left
        self.right = right
import queue
class Solution(object):

    def hasPathSum(self, root, sum):

        return self.dfs(root,0,sum)
    def dfs(self,node,currenct_sum,sum):
        if not node.left and not node.right:
            currenct_sum += node.val
            if currenct_sum == sum:
                return True
            else:
                return False
        if node.left:
            if self.dfs(node.left,currenct_sum+node.val,sum):
                return True
            else:
                pass
        if node.right:
            if self.dfs(node.right,currenct_sum+node.val,sum):
                return True
            else:
                pass

#
# def test():
#     a = TreeNode(1)
#     b = TreeNode(2)
#     c = TreeNode(2)
#     d = TreeNode(3)
#     e = TreeNode(3)
#     a.left = b
#     a.right = c
#     b.right = d
#     c.right = e
#     s = Solution()
#     print(s.isSymmetric(a))
# def test2():
#     a = TreeNode(1)
#     b = TreeNode(2)
#     c = TreeNode(2)
#     d = TreeNode(3)
#     e = TreeNode(4)
#     f = TreeNode(4)
#     g = TreeNode(3)
#
#     a.left = b
#     a.right = c
#     b.left = d
#     b.right = e
#     c.left = f
#     c.right = g
#     s = Solution()
#     print(s.isSymmetric(a))
# def test3():
#     a = TreeNode(1)
#
#     s = Solution()
#     print(s.isSymmetric(a))
# def test4():
#     a = TreeNode(1)
#
#     s = Solution()
#     print(s.isSymmetric(None))

# def test0():
#     a = TreeNode(5)
#     b = TreeNode(4)
#     c = TreeNode(8)
#     a.left = b
#     a.right = c
#     d = TreeNode(11)
#     b.left = d
#     e = TreeNode(13)
#     c.left = e
#     f = TreeNode(4)
#     c.right = f
#     g = TreeNode(7)
#     d.left = g
#     h = TreeNode(2)
#     d.right = h
#     i = TreeNode(1)
#     f.right = i
#     s = Solution()
#     s.hasPathSum(a,22)
# test0()
def test():
    a = TreeNode(5,
                 TreeNode(4,
                          TreeNode(11,
                                   TreeNode(7,None,None),
                                   TreeNode(2,None,None)),
                          None),
                 TreeNode(8,
                          TreeNode(13,None,None),
                          TreeNode(4,
                                   None,
                                   TreeNode(1,None,None)
                                   )
                          )
                 )
    s = Solution()
    print(s.hasPathSum(a,26))
test()
# test2()
# test3()
# test4()