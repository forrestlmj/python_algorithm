# Definition for a binary tree node.
import queue
class TreeNode:
    def __init__(self, x,l,r):
        self.val = x
        self.left = l
        self.right = r

class BSTIterator:

    def __init__(self, root: TreeNode):
        self.l = [None, ]
        self.idx = 0
        s = queue.deque()
        if not root:
            return
        s.append(root)
        self.dfs(root)
        return
    def dfs(self,cur):
        if not cur.left and not cur.right:
            self.l.append(cur.val)
            return
        if cur.left:
            self.dfs(cur.left)
            # self.l.append(cur.left.val)
        self.l.append(cur.val)
        if cur.right:
            self.dfs(cur.right)
            # self.l.append(cur.right.val)
        return
    def next(self) -> int:
        """
        @return the next smallest number
        """
        if self.hasNext():
            self.idx += 1
            return self.l[self.idx]
        else:
            return None
    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        if self.idx+1 < len(self.l):
            return True
        else:
            return False

# Your BSTIterator object will be instantiated and called as such:


def test0():
    root = None
    obj = BSTIterator(root)
    print( obj.next())
    print( obj.hasNext())
def test1():
    root = TreeNode(7,
                    TreeNode(3,None,None),
                    TreeNode(15,
                                TreeNode(9,None,None),
                                TreeNode(20,None,None)
                             )
                    )
    iterator  = BSTIterator(root)
    print(iterator.next()) #  return 3
    print(iterator.next()) #  return 7
    print(iterator.hasNext()) #  return true
    print(iterator.next()) #  return 9
    print(iterator.hasNext()) #  return true
    print(iterator.next()) #  return 15
    print(iterator.hasNext()) #  return true
    print(iterator.next()) #  return 20
    print(iterator.hasNext()) #  return false

if __name__ == "__main__":
    test0()
    test1()