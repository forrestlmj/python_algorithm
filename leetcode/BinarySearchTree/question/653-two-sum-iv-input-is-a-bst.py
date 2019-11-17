# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    l = list()
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def dfs(root):
            if not root:
                return None
            dfs(root.left)
            self.l.append(root.val)
            dfs(root.right)
        if not root:
            return False
        self.l = list()
        dfs(root)
        print(self.l)
        a,b = 0,len(self.l)-1
        while(a<b):
            if k == self.l[a]+self.l[b]:
                return True
            elif k < self.l[a]+self.l[b]:
                b -= 1
            elif k > self.l[a]+self.l[b]:
                a += 1
        return False