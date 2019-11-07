# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
import queue
class Solution(object):
    def notSymmetric(self,l):
        return l != l[::-1]
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        q = queue.deque()
        q.append((root,0))
        node_list = list()
        while len(q) > 0:
            cur,level = q.popleft()
            if len(node_list) == level:
                node_list.append([])
                node_list[level].append(cur.val if cur else None)
            else:
                node_list[level].append(cur.val if cur else None)

            if cur:
                q.append((cur.left,level+1))
                q.append((cur.right,level+1))
        for i in node_list:
            if self.notSymmetric(i):
                return False
        return True
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