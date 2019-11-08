# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import queue
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isMirror(root,root)
    def isMirror(self,a,b):
        if not a and not b:
            return True
        elif not a or not b:
            return False
        else:
            return a.val == b.val and self.isMirror(a.left,b.right) and self.isMirror(a.right,b.left)
def test():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(2)
    d = TreeNode(3)
    e = TreeNode(3)
    a.left = b
    a.right = c
    b.right = d
    c.right = e
    s = Solution()
    print(s.isSymmetric(a))
def test2():
    a = TreeNode(1)
    b = TreeNode(2)
    c = TreeNode(2)
    d = TreeNode(3)
    e = TreeNode(4)
    f = TreeNode(4)
    g = TreeNode(3)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g
    s = Solution()
    print(s.isSymmetric(a))
def test3():
    a = TreeNode(1)

    s = Solution()
    print(s.isSymmetric(a))
def test4():
    a = TreeNode(1)

    s = Solution()
    print(s.isSymmetric(None))

test()
test2()
test3()
test4()