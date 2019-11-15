# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def dfs(root,p):
            if not root:
                return
            if not root.left and not root.right:
                return l.append(p+str(root.val))
            if root.left:
                dfs(root.left, p+str(root.val))
            if root.right:
                dfs(root.right, p+str(root.val))
            return
        l = list()
        dfs(root,"")
        ans = 0
        for num in l:
            print(num)
            v = 0
            num = num[::-1]
            for c in range(len(num)):
                v = v+ (2 ** c if num[c] =="1"  else 0)
            print(v)
            ans +=v
        return ans